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
    PLAIN: lambda tree: plain_render(tree, ''),
    STYLISH: lambda tree: stylish_render(tree, 1),
}


def render(
    ast: List[dict],
    format_name: str = STYLISH,
) -> str:
    """Return the formatter based on the specified format."""
    return formats[format_name](ast)
