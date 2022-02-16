"""Gendiff Formaters Module."""

import json
from typing import List

from gendiff.formaters.plain_formater import render as plain_render
from gendiff.formaters.stylish_formater import render as stylish_render

JSON = 'json'
PLAIN = 'plain'
STYLISH = 'stylish'

formats = {
    JSON: json.dumps,
    PLAIN: plain_render,
    STYLISH: stylish_render,
}


def render(ast: List[dict], format_name: str) -> str:
    """Return the formatter based on the specified format."""
    if not formats.get(format_name):
        raise ValueError(
            'The unknown format of output ({0}).'.format(format_name),
        )

    return formats[format_name](ast)
