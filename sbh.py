'''
Salt Bae Hash

Plain Text -> Cipher(s) -> Hash(s)

Github.com/OGLinuk/sbh

Inspired by my tutor Mark during my second year BIT Security class
'''

import os
import sys
import time
import hashlib
import logging
import random as rng
from string import ascii_lowercase, digits, printable

class SaltBaeHash(object):
    '''SaltBaeHash'''

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ascii_symbols = printable[62:] # Using the symbols section of string.printable
        self.logger = self.load_logger()
        self.menu()

    def load_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s/%(name)s/%(levelname)s/%(message)s')
        file_handler = logging.FileHandler('raw_sbh_logs.txt')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    # Generate a SBH string
    def generate(self):
        iters = int(input('\nNum of ciphers: '))
        plainText = input('\nPlain Text: ')
        start_time = time.time()
        rot = int(rng.randint(1, sys.maxsize))
        self.logger.info('Rotation 0: {}'.format(rot))
        hashedText = self.ccFunc(rot, plainText)
        for i in range(1, iters):
            rot = int(rng.randint(1, (sys.maxsize)))
            self.logger.info('Rotation {}: {}'.format(i, rot))
            hashedText = self.ccFunc(rot, hashedText)
        print('\nDuration: {}'.format(time.time() - start_time))
        with open('raw_sbh_logs.txt', 'r') as fIN, open('{}_rotations.txt'.format(input('\nContext: ')), 'ab+') as fOUT:
            for line in fIN.readlines():
                fOUT.write(bytes(line.split(':')[-1].lstrip(), 'UTF-8'))
        os.remove('raw_sbh_logs.txt')
        print('\nSBH: {}'.format(hashedText))
        self.doAgain()

    # Reproduce a SBH string
    def reproduce(self):
        rots = self.load_rotations()
        plainText = input('\nPlain Text: ')
        start_time = time.time()
        for rot in rots:
            plainText = self.ccFunc(rot, plainText)
        print('\nSBH: {}\n\nDuration: {}'.format(plainText, time.time() - start_time))
        self.doAgain()

    # Util func for reproduce()
    def load_rotations(self):
        with open('{}'.format(input('\nRotation File: '))) as f:
            return [int(rot) for rot in f.readlines()]

    # Caesar Cipher
    def ccFunc(self, prRotation, prPlainText):
        encryptedText = ''
        for n in prPlainText:
            if n.isalpha():
                encryptedText += ascii_lowercase[(ascii_lowercase.index(n.lower()) + prRotation) % len(ascii_lowercase)]
            elif n.isdigit():
                encryptedText += digits[(digits.index(n) + prRotation) % len(digits)]
            else:
                encryptedText += self.ascii_symbols[(self.ascii_symbols.index(n) + prRotation) % len(self.ascii_symbols)]
        return hashlib.sha256(bytes(encryptedText, 'UTF-8')).hexdigest()

    # Menu
    def menu(self):
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[H\033[2J") # another way to clear the terminal
        print('-----------------Salt Bae Hash-----------------')
        print('Plain Text -> Cipher(s) -> Hash(s)')
        choice = int(input('\n1) Generate\n2) Reproduce\n\n'))
        if choice == 1:
            self.generate()
        elif choice == 2:
            self.reproduce()
        else:
            print('No no no ...')
            time.sleep(3)
            self.menu()

    # Repeat program
    def doAgain(self):
        choice = input('\nSBH another one? [Y/n]: ')
        if choice.lower() == 'y':
            self.menu()
        elif choice.lower() == 'n':
            sys.exit(0)
        else:
            self.doAgain()
