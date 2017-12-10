'''
Entry point for SaltBaeHash
'''

import sys
from sbh import SaltBaeHash

def main(argv):
    sbh = SaltBaeHash(argv)

if __name__ == '__main__':
    main(sys.argv[1:])
