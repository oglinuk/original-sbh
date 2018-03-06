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
import argparse
import random as rng
from string import ascii_lowercase, digits, printable

class SaltBaeHash(object):
    '''SaltBaeHash'''

    def __init__(self, args):
        self.args = args
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
    def generate(self, args):
        if args == None:
            iters = int(input('\nNum of ciphers: '))
            plainText = input('\nPlain Text: ')
        else:
            iters = int(args[0])
            plainText = args[1]
        start_time = time.time()
        rot = int(rng.randint(1, sys.maxsize))
        self.logger.info('Rotation 0: {}'.format(rot))
        hashedText = self.ccFunc(rot, plainText)
        for i in range(1, iters):
            rot = int(rng.randint(1, sys.maxsize))
            self.logger.info('Rotation {}: {}'.format(i, rot))
            hashedText = self.ccFunc(rot, hashedText)
        print('\nDuration: {}'.format(time.time() - start_time))
        context = input('\nContext: ')
        try:
            with open('raw_sbh_logs.txt', 'r+') as fIN, open('{}_rots.txt'.format(context), 'ab+') as fOUT:
                for line in fIN.readlines():
                    fOUT.write(bytes(line.split(':')[-1].lstrip(), 'UTF-8'))
        except Exception as e:
            print(str(e))
        finally:
            self.encryption('{}_rots.txt'.format(context))
            os.remove('raw_sbh_logs.txt')
        print('\nSBH: {}'.format(hashedText))
        self.doAgain()

    # Reproduce a SBH string
    def reproduce(self, args):
        rot_file = None
        if args == None:
            rot_file = input('File name: ')
            rots = self.load_rotations(rot_file)
            plainText = input('\nPlain Text: ')
        else:
            rot_file = args[0]
            rots = self.load_rotations(rot_file)
            plainText = args[1]
        start_time = time.time()
        for rot in rots:
            plainText = self.ccFunc(rot, plainText)
        os.remove('{}.txt'.format(rot_file.split('.')[0]))
        print('\nSBH: {}\n\nDuration: {}'.format(plainText, time.time() - start_time))
        self.doAgain()

    # Util func for reproduce()
    def load_rotations(self, args):
        if '.enc' in args:
            self.encryption(args)
            args = '{}.txt'.format(args.split('.')[0])
        with open('{}'.format(args), 'r+') as f:
            return [int(rot) for rot in f.readlines()]

    # Encrypton and decryption w/ AES 256 of SBH rotation files
    def encryption(self, args):
        if '.enc' not in args:
            os.system('sudo openssl aes-256-cbc -in {} -out {}'.format(args, '{}.enc'.format(args.split('.')[0])))
            os.remove(args)
        else:
            os.system('sudo openssl aes-256-cbc -d -in {} -out {}'.format(args, '{}.txt'.format(args.split('.')[0])))

    # Caesar cipher
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
        # https://stackoverflow.com/a/2084628
        os.system('cls' if os.name == 'nt' else 'clear')
        #print("\033[H\033[2J") # another way to clear the terminal
        print('-----------------Salt Bae Hash-----------------')
        print('Plain Text -> Cipher(s) -> Hash(s)')
        if len(sys.argv) <= 1:
            choice = int(input('\n1) Generate\n2) Reproduce\n3) Learn about AES\n\n'))
            if choice == 1:
                self.generate(None)
            elif choice == 2:
                self.reproduce(None)
            elif choice == 3:
                self.learn_about_aes()
            else:
                print('No no no ...')
                time.sleep(3)
                self.menu()
        else:
            if self.args.generate:
                self.generate(self.args.generate)
            elif self.args.reproduce:
                self.reproduce(self.args.reproduce)

    # Util for Encryption choice -> provides download of AES publications
    def learn_about_aes(self):
        os.system('wget https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf')
        self.doAgain()

    # Repeat program
    def doAgain(self):
        self.args = None
        choice = input('\nSBH another one? [Y/n]: ')
        if choice.lower() == 'y':
            self.menu()
        elif choice.lower() == 'n':
            sys.exit(0)
        else:
            print('No no no ...')
            time.sleep(3)
            self.doAgain()
