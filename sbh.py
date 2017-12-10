'''
Salt Bae Hash

Plain Text -> Cipher(s) -> Hash(s)

Github.com/OGLinuk/sbh

Inspired by my tutor Mark during my second year BIT Security class
'''

import os
import sys
import hashlib
from string import ascii_lowercase, digits, printable

class SaltBaeHash(object):
    '''SaltBaeHash'''

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ascii_symbols = printable[62:] # Using the symbols section of string.printable
        self.sbhText = '' # Need to figure out why this produces a dif hash than encryptedText
        self.menu()

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
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-----------------Salt Bae Hash-----------------')
            print('Plain Text -> Cipher(s) -> Hash(s)')
            if self.args != ([],):
                hashedText = self.ccFunc(int(self.args[0][2]), self.args[0][1])
                for i in range(1, int(self.args[0][0])):
                    hashedText = self.ccFunc(int(self.args[0][i+2]), hashedText)
                print('\nSBH: {}'.format(hashedText))

            else:
                iters = int(input('\nNum of ciphers: '))
                plainText = input('\nPlain Text: ')
                hashedText = self.ccFunc(int(input('\nRotation: ')), plainText)
                for i in range(1, iters):
                    hashedText = self.ccFunc(int(input('Rotation: ')), hashedText)
                print('\nSBH: {}'.format(hashedText))
            input('\nPress any key to SBH another plain text ...')
            self.args = ([],)
            self.menu()

    # Repeat choice
    def doAgain(self):
        choice = input('\nSBH another plain text? [Y/n]: ')
        if choice.lower() == 'y':
            self.menu()
        elif choice.lower() == 'n':
            sys.exit(0)
        else:
            self.doAgain()
