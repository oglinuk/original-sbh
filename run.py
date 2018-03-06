'''
Entry point for SaltBaeHash
'''

import argparse
from sbh import SaltBaeHash

def main(args):
    sbh = SaltBaeHash(args)

if __name__ == '__main__':
    # https://docs.python.org/2/library/argparse.html#description
    parser = argparse.ArgumentParser(description='-----SaltBaeHash CLI-----')
    parser.add_argument('-g', '--generate', nargs='*', help='Generate a SBH string -> [nCiphers] [plainText]')
    parser.add_argument('-r', '--reproduce', nargs='*', help='Reproduce a SBH string -> [inFile] [plainText]')
    main(parser.parse_args())
