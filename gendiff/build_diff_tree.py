"""Gendiff AST Module."""

from typing import Callable

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
NESTED = 'nested'
UNCHENGED = 'unchanged'


def build_tree_node(
    key: str,
    first_dict: dict,
    second_dict: dict,
    function: Callable[[dict, dict], list],
) -> dict:
    """Build node for diff."""
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


def build_diff_tree(first: dict, second: dict) -> list:
    """Build diff between two dictionaries."""
    uniq_keys = sorted(first.keys() | second.keys())

    ast = (
        build_tree_node(key, first, second, build_diff_tree)
        for key in uniq_keys
    )

    return list(ast)
