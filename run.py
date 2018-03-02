'''
Entry point for SaltBaeHash
'''

import argparse
from sbh import SaltBaeHash

def main(args):
    sbh = SaltBaeHash(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for SBH')
    parser.add_argument('-g', '--generate', nargs='*', help='Generate a SBH string -> [nCiphers] [plainText]')
    parser.add_argument('-r', '--reproduce', nargs='*', help='Reproduce a SBH string -> [inFile] [plainText]')
    parser.add_argument('-e', '--encrypt', nargs='*', help='Encrypt a SBH rot file -> [inFile] [outFile]')
    parser.add_argument('-d', '--decrypt', nargs='*', help='Decrypt a SBH rot file -> [inFIle] [outFile]')
    main(parser.parse_args())
