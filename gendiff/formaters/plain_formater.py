"""Gendiff Plain Formater Module."""

from typing import Callable, Union

from gendiff.formaters.common import transform_value

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
NESTED = 'nested'
UNCHENGED = 'unchanged'


def stringify(node_data: Union[str, int, bool, None, dict]) -> str:
    """
    Stringify data.

    Args:
        node_data: any

    Returns:
        str
    """
    if isinstance(node_data, str):
        return "'{0}'".format(node_data)

    return (
        '[complex value]'
        if isinstance(node_data, dict)
        else transform_value(node_data)
    )


def get_action_by_type(
    node: dict,
    parent: str,
    function: Callable[[list, str], str],
) -> str:
    """
    Transform node based on node's type.

    Args:
        node: dict
        parent: str
        function: fn

    Returns:
        str
    """
    node_type = node['type']
    node_name = node['name']

    if node_type == NESTED:
        return function(node['children'], '{0}{1}.'.format(parent, node_name))
    if node_type == DELETED:
        return "Property '{0}{1}' was removed".format(parent, node_name)
    if node_type == ADDED:
        return "Property '{0}{1}' was added with value: {2}".format(
            parent,
            node_name,
            stringify(node['value']),
        )

    return "Property '{0}{1}' was updated. From {2} to {3}".format(
        parent,
        node_name,
        stringify(node['value_before']),
        stringify(node['value_after']),
    )


def render(ast: list, parent: str) -> str:
    """
    Render AST to string.

    Args:
        ast: list
        parent: str

    Returns:
        str
    """
    filtered = filter(lambda node: node['type'] != UNCHENGED, ast)
    output = map(
        lambda node: get_action_by_type(node, parent, render),
        filtered,
    )

    return '\n'.join(output)
