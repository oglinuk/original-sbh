'''
Salt Bae Hashing Function
Plain Text -> Cipher(s) -> Hash(s)

Github.com/OGLinuk/sbh

Inspired by my tutor Mark during my second year Security class
'''
import os
import sys
from string import ascii_lowercase, digits, printable
import hashlib

SYMBOLS = printable[62:]

def rotFunc(prRotation, prPlainText):
    prPlainText = prPlainText.replace(' ', '')
    encryptedText = ''
    for n in prPlainText:
        if n.isalpha():
            encryptedText += ascii_lowercase[(ascii_lowercase.index(n.lower()) + prRotation) % len(ascii_lowercase)]
        elif n.isdigit():
            encryptedText += digits[(digits.index(n) + prRotation) % len(digits)]
        else:
            encryptedText += SYMBOLS[(SYMBOLS.index(n) + prRotation) % len(SYMBOLS)]
    return hashlib.sha256(bytes(encryptedText, 'UTF-8')).hexdigest()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-----------------Salt Bae Hash-----------------')
        print('Plain Text -> Cipher(s) -> Hash(s)')
        plainText = input('Plain Text: ')
        iters = int(input('Num of ciphers: '))
        text = rotFunc(int(input('Rotation: ')), plainText)
        for i in range(1, iters):
            text = rotFunc(int(input('Rotation: ')), text)
        print('Salt Bae Encrypted String: {}'.format(text))
        input('\nPress enter to sbh another plain text input ...')

if __name__ == '__main__':
    main()
