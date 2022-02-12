#!/usr/bin/env python

"""Gendiff Main Script."""

import argparse

from gendiff.formaters.render import JSON, PLAIN, STYLISH
from gendiff.generate_diff import generate_diff

DESCRIPTION = 'Generate diff'
HELP_MESSAGE = 'set format of output'


def main():
    """Run Gendiff script."""
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help=HELP_MESSAGE,
        choices=[STYLISH, PLAIN, JSON],
        default=STYLISH,
    )

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
