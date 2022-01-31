"""Gendiff Formaters Module."""

from gendiff.formaters.stylish_formater import render as stylish_render


def render(ast, style='stylish'):
    """
    Кeturn the formatter based on the specified style.

    Args:
        ast: dict
        style: str

    Returns:
        fn
    """
    if style == 'stylish':
        return stylish_render(ast, 1)
