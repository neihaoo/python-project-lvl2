"""Gendiff Parsers Module."""

import json

import yaml

JSON = 'json'
YAML = 'yaml'

parsers = {
    JSON: json.loads,
    YAML: yaml.safe_load,
}


def parse(input_data: str, data_format: str) -> dict:
    """Parse input data."""
    if data_format in {'yaml', 'yml'}:
        data_format = 'yaml'

    if not parsers.get(data_format):
        raise ValueError('The {0} format is not supported.'.format(data_format))

    return parsers[data_format](input_data)
