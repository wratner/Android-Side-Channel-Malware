#!/usr/bin/env python

from PktReader import *
from SigChecker import *
import sys


def main():
    reader = PktReader(sys.argv[1])
    check = SigChecker(reader)
    print check.generate_guess()

if __name__ == '__main__':
    main()
