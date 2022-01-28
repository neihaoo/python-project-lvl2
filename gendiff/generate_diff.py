"""Gendiff Module."""

import os

from gendiff.parsers import parse as parse_file


def prepare_file(path):
    """
    Prepare input file.

    Args:
        path: str

    Returns:
        dict
    """
    with open(path) as filename:
        _, extension = os.path.splitext(path)

        return parse_file(filename, extension[1:])


def generate_diff(first_file, second_file):
    """
    Generate diff between two JSON files.

    Args:
        first_file: str
        second_file: str

    Returns:
        str
    """
    first = prepare_file(first_file)
    second = prepare_file(second_file)

    diff = []

    for key in sorted(first.keys() | second.keys()):
        if key not in second:
            diff.append(' - {0}: {1}'.format(key, first[key]))
        elif key not in first:
            diff.append(' + {0}: {1}'.format(key, second[key]))
        elif first[key] == second[key]:
            diff.append('   {0}: {1}'.format(key, first[key]))
        else:
            diff.append(' - {0}: {1}\n  + {0}: {2}'.format(
                key, first[key], second[key],
            ))

    return '{{\n {0}\n}}'.format('\n '.join(diff))
