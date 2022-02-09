"""Gendiff Parsers Module."""

import json

import yaml

parsers = {
    'json': json.loads,
    'yaml': yaml.safe_load,
}


def parse(path: str, extension: str) -> dict:
    """
    Parse input files.

    Args:
        path: str
        extension: str

    Returns:
        dict
    """
    if extension in {'yaml', 'yml'}:
        extension = 'yaml'

    return parsers[extension](path)
