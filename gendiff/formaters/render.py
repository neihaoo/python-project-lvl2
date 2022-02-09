"""Gendiff Formaters Module."""

import json

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
    ast: list,
    format_name: str = STYLISH,
) -> str:
    """
    Кeturn the formatter based on the specified format.

    Args:
        ast: dict
        format_name: str

    Returns:
        str
    """
    return formats[format_name](ast)
