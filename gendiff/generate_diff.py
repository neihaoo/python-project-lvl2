"""Gendiff Module."""

import os
from typing import Tuple

from gendiff.build_diff_tree import build_diff_tree
from gendiff.formaters.render import STYLISH, render
from gendiff.parsers import parse as parse_file


def read_file(path: str) -> Tuple[str, str]:
    """Prepare input file."""
    with open(path) as filename:
        _, extension = os.path.splitext(path)

        return (filename.read(), extension[1:])


def generate_diff(
    first_file: str,
    second_file: str,
    format_name: str = STYLISH,
) -> str:
    """Generate diff between two files."""
    first = parse_file(*read_file(first_file))
    second = parse_file(*read_file(second_file))
    diff = build_diff_tree(first, second)

    return render(diff, format_name)
