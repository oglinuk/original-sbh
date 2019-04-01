import os
import random
import sys
from string import ascii_lowercase, digits, printable
import hashlib

SYMBOLS = printable[62:]

def rotFunc(rot, plaintext):
    plaintext = plaintext.replace(' ', '')
    encrypted = ''
    for n in plaintext:
        if n.isalpha():
            encrypted += ascii_lowercase[(ascii_lowercase.index(n.lower()) + rot) % len(ascii_lowercase)]
        elif n.isdigit():
            encrypted += digits[(digits.index(n) + rot) % len(digits)]
        else:
            encrypted += SYMBOLS[(SYMBOLS.index(n) + rot) % len(SYMBOLS)]
    return hashlib.sha256(bytes(encrypted, 'UTF-8')).hexdigest()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-----------------Salt Bae Hash-----------------')
        print('Plain Text -> N Cipher(s) -> Seed -> Hash(s)')
        plainText = input('Plain Text: ')
        iters = int(input('Number of Ciphers: '))
        random.seed(int(input('Seed: ')))
        rot = random.randint(1, sys.maxsize)
        print(rot)
        text = rotFunc(rot, plainText)
        for _ in range(1, iters):
            random.seed(rot)
            rot = random.randint(1, sys.maxsize)
            text = rotFunc(rot, text)
        print('Salt Bae Encrypted String: {}'.format(text))
        input('\nPress enter to sbh another plain text input ...')

if __name__ == '__main__':
    main()
