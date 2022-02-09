"""Gendiff Module."""

import os

from gendiff.build_ast import build_ast_diff
from gendiff.formaters.render import render
from gendiff.parsers import parse as parse_file

STYLISH = 'stylish'


def read_file(path: str) -> tuple:
    """
    Prepare input file.

    Args:
        path: str

    Returns:
        tuple
    """
    with open(path) as filename:
        _, extension = os.path.splitext(path)

        return (filename.read(), extension[1:])


def generate_diff(
    first_file: str,
    second_file: str,
    format_name: str = STYLISH,
) -> str:
    """
    Generate diff between two files.

    Args:
        first_file: str
        second_file: str
        format_name: str

    Returns:
        str
    """
    first = parse_file(*read_file(first_file))
    second = parse_file(*read_file(second_file))
    ast = build_ast_diff(first, second)

    return render(ast, format_name)
