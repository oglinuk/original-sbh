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
        with open('raw_sbh_logs.txt', 'r') as fIN, open('{}_rotations.txt'.format(input('\nContext: ')), 'ab+') as fOUT:
            for line in fIN.readlines():
                fOUT.write(bytes(line.split(':')[-1].lstrip(), 'UTF-8'))
        os.remove('raw_sbh_logs.txt')
        print('\nSBH: {}'.format(hashedText))
        self.doAgain()

    # Reproduce a SBH string
    def reproduce(self, args):
        if args == None:
            rots = self.load_rotations(None)
            plainText = input('\nPlain Text: ')
        else:
            rots = self.load_rotations(args[0])
            plainText = args[1]
        start_time = time.time()
        for rot in rots:
            plainText = self.ccFunc(rot, plainText)
        print('\nSBH: {}\n\nDuration: {}'.format(plainText, time.time() - start_time))
        self.doAgain()

    # Util func for reproduce()
    def load_rotations(self, args):
        if args == None:
            in_file = input('\nRotation File: ')
            if in_file.endswith('.enc'):
                self.encryption('-d', in_file, '{}.txt'.format(in_file.split('.')[0]))
                in_file = '{}.txt'.format(in_file.split('.')[0])
            with open('{}'.format(in_file), 'r') as f:
                return [int(rot) for rot in f.readlines()]
        else:
            with open('{}'.format(args), 'r') as f:
                return [int(rot) for rot in f.readlines()]

    # Encrypton and decryption of SBH rotation files
    def encryption(self, args):
        if args == None:
            choice = input('\n(E)ncrypt or (D)ecrypt\n\n')
            if choice.lower() == 'e':
                # Reason for the difference is because we ONLY want to remove the .txt file version of SBH rot files
                in_file = input('\nIn File: ')
                # https://askubuntu.com/questions/60712/how-do-i-quickly-encrypt-a-file-with-aes
                os.system('sudo openssl aes-256-cbc -in {} -out {}'.format(in_file, input('\nOut File: ')))
                os.remove(in_file)
            elif choice.lower() == 'd':
                os.system('sudo openssl aes-256-cbc -d -in {} -out {}'.format(input('\nIn File: '), input('\nOut File: ')))
        else:
            if args.encrypt:
                os.system('sudo openssl aes-256-cbc -in {} -out {}'.format(args.encrypt[0], args.encrypt[1]))
                os.remove(args.encrypt[0])
            elif args.decrypt:
                os.system('sudo openssl aes-256-cbc -d -in {} -out {}'.format(args.decrypt[0], args.decrypt[1]))
        self.doAgain()

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
        os.system('cls' if os.name == 'nt' else 'clear')
        #print("\033[H\033[2J") # another way to clear the terminal
        print('-----------------Salt Bae Hash-----------------')
        print('Plain Text -> Cipher(s) -> Hash(s)')
        if self.args.generate != None or self.args.reproduce != None or self.args.encrypt != None or self.args.decrypt != None:
            if self.args.generate:
                self.generate(self.args.generate)
            elif self.args.reproduce:
                self.reproduce(self.args.reproduce)
            elif self.args.encrypt:
                self.encryption(self.args)
            elif self.args.decrypt:
                self.encryption(self.args)
        else:
            choice = int(input('\n1) Generate\n2) Reproduce\n3) Encryption\n\n'))
            if choice == 1:
                self.generate(None)
            elif choice == 2:
                self.reproduce(None)
            elif choice == 3:
                self.learn_about_aes()
                self.encryption(None)
            else:
                print('No no no ...')
                time.sleep(3)
                self.menu()

    # Util for Encryption choice -> provides download of AES publications
    def learn_about_aes(self):
        choice = input('\nLearn more about AES encryption? [Y/n]: ')
        if choice.lower() == 'y':
            os.system('wget https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf')
        return

    # Repeat program
    def doAgain(self):
        choice = input('\nSBH another one? [Y/n]: ')
        if choice.lower() == 'y':
            self.menu()
        elif choice.lower() == 'n':
            sys.exit(0)
        else:
            self.doAgain()
