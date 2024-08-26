#!/usr/bin/env python3
"""Command line program for generating secure passwords using true random
number generation.
"""

from sys import argv
from secrets import choice

HELP = """
Description
    Generate a random password of specified length.

Usage
    ./passwordgen.py <LENGTH>

    <LENGTH>    The length of the generated password, a positive integer.
"""

# All printable ASCII characters excluding <space>
CHARS = ''.join(chr(i) for i in range(33, 127))

def main():
    if len(argv) <= 1:
        print(HELP)
        return
    length = int(argv[1])
    password = ''.join(choice(CHARS) for _ in range(length))
    print(password)

main()

