"""Gendiff Parsers Module."""

import json

import yaml

JSON = 'json'
YAML = 'yaml'

parsers = {
    JSON: json.loads,
    YAML: yaml.safe_load,
}


def parse(file_data: str, extension: str) -> dict:
    """Parse input data."""
    if not parsers.get(extension):
        raise ValueError('The {0} format is not supported.'.format(extension))

    return parsers[extension](file_data)
