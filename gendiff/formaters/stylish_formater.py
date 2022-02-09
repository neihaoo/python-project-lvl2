"""Gendiff Stylish Formater Module."""

import itertools
from typing import Callable, Union

from gendiff.formaters.common import transform_value

ADDED = 'added'
DELETED = 'deleted'
NESTED = 'nested'
UNCHENGED = 'unchanged'


def set_indent(depth: int = 0) -> str:
    """
    Set indent.

    Args:
        depth: int

    Returns:
        str
    """
    return '  ' * depth


def stringify(node_data: Union[str, int, bool, None, dict], depth: int) -> str:
    """
    Stringify data.

    Args:
        node_data: str | int | bool | None | dict
        depth: int

    Returns:
        str
    """
    if not isinstance(node_data, dict):
        return transform_value(node_data)

    current_indent = set_indent(depth + 1)
    deep_indent_depth = depth + 2
    deep_indent = set_indent(deep_indent_depth + 1)

    processed_data = map(
        lambda data_key, data_value: '{0}{1}: {2}'.format(
            deep_indent,
            data_key,
            stringify(data_value, deep_indent_depth),
        ),
        node_data.keys(),
        node_data.values(),
    )

    output = itertools.chain(
        '{',
        processed_data,
        ['{0}{1}'.format(current_indent, '}')],
    )

    return '\n'.join(output)


def format_node(
    node_key: str,
    node_value: Union[str, int, bool, None, dict],
    depth: int = 0,
    mark: str = '',
) -> str:
    """
    Format data to string.

    Args:
        node_key: str
        node_value: any
        depth: int
        mark: str

    Returns:
        str
    """
    return '{0}{1} {2}: {3}'.format(
        set_indent(depth),
        mark,
        node_key,
        stringify(node_value, depth),
    )


def get_action_by_type(
    node: dict,
    depth: int,
    function: Callable[[list, int], str],
) -> str:
    """
    Transform node based on node's type.

    Args:
        node: dict
        depth: int
        function: fn

    Returns:
        str
    """
    node_type = node['type']
    node_name = node['name']

    if node_type == NESTED:
        return '  {0}{1}: {2}'.format(
            set_indent(depth),
            node_name,
            function(node['children'], depth + 2),
        )
    if node_type == DELETED:
        return format_node(node_name, node['value'], depth, '-')
    if node_type == ADDED:
        return format_node(node_name, node['value'], depth, '+')
    if node_type == UNCHENGED:
        return format_node(node_name, node['value'], depth, ' ')

    return '\n'.join(
        [
            format_node(node_name, node['value_before'], depth, '-'),
            format_node(node_name, node['value_after'], depth, '+'),
        ],
    )


def render(ast: list, depth: int = 0) -> str:
    """
    Render AST to string.

    Args:
        ast: list
        depth: int

    Returns:
        str
    """
    output = map(lambda node: get_action_by_type(node, depth, render), ast)

    return '{{\n{0}\n{1}}}'.format('\n'.join(output), set_indent(depth - 1))
