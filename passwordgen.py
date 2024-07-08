#!/usr/bin/env python3
"""Command line program for generating secure passwords.

Prints a randomly generated password of a given length to the console.

Usage:
    ./passwordgen.py [<password length>]

    <password length> :
        A positive integer. If omitted, a default length is used.

Notes
-----
Uses true random number generation for security.
"""

from sys import argv
from secrets import choice

DEFAULT_LENGTH = 20

# All printable ASCII characters excluding <space>
CHARS = ''.join(chr(i) for i in range(33, 127))

length = DEFAULT_LENGTH if len(argv) <= 1 else int(argv[1])
password = ''.join(choice(CHARS) for _ in range(length))
print(password)

