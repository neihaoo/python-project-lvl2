"""Gendiff Parsers Module."""

import json

import yaml


def parse(path, extension):
    """
    Parse input files.

    Args:
        path: str
        extension: str

    Returns:
        dict
    """
    if extension in {'yaml', 'yml'}:
        return yaml.safe_load(path)
    if extension == 'json':
        return json.load(path)
