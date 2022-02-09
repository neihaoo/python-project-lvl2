"""Gendiff AST Module."""

from typing import Callable

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
NESTED = 'nested'
UNCHENGED = 'unchanged'


def build_ast_node(
    key: str,
    first_dict: dict,
    second_dict: dict,
    function: Callable[[dict, dict], list],
) -> dict:
    """
    Build node for AST.

    Args:
        key: str
        first_dict: dict
        second_dict: dict
        function: fn

    Returns:
        dict
    """
    first_value = first_dict.get(key)
    second_value = second_dict.get(key)

    if key not in second_dict:
        return {'type': DELETED, 'name': key, 'value': first_value}
    if key not in first_dict:
        return {'type': ADDED, 'name': key, 'value': second_value}
    if isinstance(first_value, dict) and isinstance(second_value, dict):
        return {
            'type': NESTED,
            'name': key,
            'children': function(first_value, second_value),
        }
    if first_value == second_value:
        return {'type': UNCHENGED, 'name': key, 'value': first_value}

    return {
        'type': CHANGED,
        'name': key,
        'value_before': first_value,
        'value_after': second_value,
    }


def build_ast_diff(first: dict, second: dict) -> list:
    """
    Generate AST diff between two dictionaries.

    Args:
        first: dict
        second: dict

    Returns:
        list
    """
    uniq_keys = sorted(first.keys() | second.keys())

    ast = map(
        lambda key: build_ast_node(key, first, second, build_ast_diff),
        uniq_keys,
    )

    return list(ast)
