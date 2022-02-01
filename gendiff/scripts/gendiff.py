#!/usr/bin/env python

"""Gendiff Main Script."""

import argparse

from gendiff.generate_diff import generate_diff


def main():
    """Run Gendiff script."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        choices=['stylish', 'plain'],
        default='stylish',
    )

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
