"""Gendiff Module."""

import os

from gendiff.build_ast import build_ast
from gendiff.formaters.render import render
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


def generate_diff(first_file, second_file, format_name='stylish'):
    """
    Generate diff between two files.

    Args:
        first_file: str
        second_file: str
        format_name: str

    Returns:
        str
    """
    first = prepare_file(first_file)
    second = prepare_file(second_file)
    ast = build_ast(first, second)

    return render(ast, format_name)
