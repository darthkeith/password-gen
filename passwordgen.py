#!/usr/bin/env python3
"""Command line program for generating secure passwords using true random
number generation.
"""

from sys import argv
from secrets import choice

HELP = """
Description:
    Generate a random password of specified length.

Usage:
    ./passwordgen.py <LENGTH> [EXCLUDED]

Arguments:
    <LENGTH>
        The length of the generated password, a positive integer.
    [EXCLUDED]
        (Optional) A string of characters to be excluded from the password.
"""

# All printable ASCII characters excluding <space>
BASE_CHARS = "".join(chr(i) for i in range(33, 127))


def main():
    if len(argv) <= 1:
        print(HELP)
        return
    length = int(argv[1])
    excluded = set(argv[2]) if len(argv) >= 3 else set()
    chars = "".join(c for c in BASE_CHARS if c not in excluded)
    password = "".join(choice(chars) for _ in range(length))
    print(password)


main()

