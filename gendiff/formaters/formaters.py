"""Gendiff Formaters Module."""

import json

from gendiff.formaters.plain_formater import render as plain_render
from gendiff.formaters.stylish_formater import render as stylish_render


def render(ast, format_name='stylish'):
    """
    Кeturn the formatter based on the specified format.

    Args:
        ast: dict
        format_name: str

    Returns:
        fn
    """
    if format_name == 'stylish':
        return stylish_render(ast, 1)
    if format_name == 'plain':
        return plain_render(ast, '')
    if format_name == 'json':
        return json.dumps(ast)
