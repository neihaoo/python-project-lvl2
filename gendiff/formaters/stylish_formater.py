"""Gendiff Stylish Formater Module."""

import itertools
from typing import Union

from gendiff.formaters.common import transform_value

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
NESTED = 'nested'
UNCHENGED = 'unchanged'

types_actions = {
    ADDED: lambda node, depth, _: format_node(
        node['name'],
        node['value'],
        depth,
        '+',
    ),
    CHANGED: lambda node, depth, _: '\n'.join(
        [
            format_node(node['name'], node['value_before'], depth, '-'),
            format_node(node['name'], node['value_after'], depth, '+'),
        ],
    ),
    DELETED: lambda node, depth, _: format_node(
        node['name'],
        node['value'],
        depth,
        '-',
    ),
    NESTED: lambda node, depth, function: '  {0}{1}: {2}'.format(
        set_indent(depth),
        node['name'],
        function(node['children'], depth + 2),
    ),
    UNCHENGED: lambda node, depth, _: format_node(
        node['name'],
        node['value'],
        depth,
        ' ',
    ),
}


def set_indent(indent_size: int = 0) -> str:
    """
    Set indent.

    Args:
        indent_size: int

    Returns:
        str
    """
    return '  ' * indent_size


def stringify(
    node_data: Union[str, int, bool, None, dict],
    indent_size: int,
) -> str:
    """
    Stringify data.

    Args:
        node_data: str | int | bool | None | dict
        indent_size: int

    Returns:
        str
    """
    if not isinstance(node_data, dict):
        return transform_value(node_data)

    current_indent = set_indent(indent_size + 1)
    deep_indent_size = indent_size + 2
    deep_indent = set_indent(deep_indent_size + 1)

    processed_data = map(
        lambda data_key, data_value: '{0}{1}: {2}'.format(
            deep_indent,
            data_key,
            stringify(data_value, deep_indent_size),
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
    indent_size: int = 0,
    mark: str = '',
) -> str:
    """
    Format data to string.

    Args:
        node_key: str
        node_value: str | int | bool | None | dict
        indent_size: int
        mark: str

    Returns:
        str
    """
    return '{0}{1} {2}: {3}'.format(
        set_indent(indent_size),
        mark,
        node_key,
        stringify(node_value, indent_size),
    )


def render(ast: list, indent_size: int = 0) -> str:
    """
    Render AST to string.

    Args:
        ast: list
        indent_size: int

    Returns:
        str
    """
    output = map(
        lambda ast_node: types_actions[ast_node['type']](
            ast_node,
            indent_size,
            render,
        ),
        ast,
    )

    return '{{\n{0}\n{1}}}'.format(
        '\n'.join(output),
        set_indent(indent_size - 1),
    )
