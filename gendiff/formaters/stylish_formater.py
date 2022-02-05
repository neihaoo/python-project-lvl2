"""Gendiff Stylish Formater Module."""

import itertools

from gendiff.formaters.common import transform_value


def set_indent(depth=0):
    """
    Set indent.

    Args:
        depth: int

    Returns:
        str
    """
    return '  ' * depth


def stringify(node_data, depth):
    """
    Stringify data.

    Args:
        node_data: any
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
            deep_indent, data_key, stringify(data_value, deep_indent_depth),
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


def format_node(node_key, node_value, depth=0, mark=''):
    """
    Farnat data to string.

    Args:
        node_key: str
        node_value: any
        depth: int
        mark: str

    Returns:
        str
    """
    return '{0}{1} {2}: {3}'.format(
        set_indent(depth), mark, node_key, stringify(node_value, depth),
    )


def get_action_by_type(node, depth, function):
    """
    Transform node based on node's type.

    Args:
        node: dict
        depth: int
        function: fn

    Returns:
        map
    """
    node_type = node.get('type')
    node_name = node.get('name')

    if node_type == 'nested':
        return '  {0}{1}: {2}'.format(
            set_indent(depth),
            node_name,
            function(node['children'], depth + 2),
        )
    if node_type == 'deleted':
        return format_node(node_name, node['value'], depth, '-')
    if node_type == 'added':
        return format_node(node_name, node['value'], depth, '+')
    if node_type == 'unchanged':
        return format_node(node_name, node['value'], depth, ' ')
    if node_type == 'changed':
        return '\n'.join([
            format_node(node_name, node['value_before'], depth, '-'),
            format_node(node_name, node['value_after'], depth, '+'),
        ])


def render(ast, depth=0):
    """
    Render AST to string.

    Args:
        ast: map
        depth: int

    Returns:
        str
    """
    output = map(lambda node: get_action_by_type(node, depth, render), ast)

    return '{{\n{0}\n{1}}}'.format('\n'.join(output), set_indent(depth - 1))
