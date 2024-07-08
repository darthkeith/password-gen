#!/usr/bin/env python3
"""Command line program for generating secure passwords.

Prints a randomly generated password of a given length to the console.

Usage:
    ./passwordgen.py <password length>

Notes
-----
Uses true random number generation for security.
"""

from sys import argv
from secrets import choice

# All printable ASCII characters excluding <space>
CHARS = ''.join(chr(i) for i in range(33, 127))

length = int(argv[1])
password = ''.join(choice(CHARS) for _ in range(length))
print(password)

