"""Gendiff Plain Formater Module."""

from gendiff.formaters.common import transform_value


def stringify(node_data):
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


def get_action_by_type(node, parent, function):
    """
    Transform node based on node's type.

    Args:
        node: dict
        parent: str
        function: fn

    Returns:
        map
    """
    if node['type'] == 'nested':
        return function(
            node['children'],
            '{0}{1}.'.format(parent, node['name']),
        )
    if node['type'] == 'deleted':
        return "Property '{0}{1}' was removed".format(parent, node['name'])
    if node['type'] == 'added':
        return "Property '{0}{1}' was added with value: {2}".format(
            parent,
            node['name'],
            stringify(node['value']),
        )
    if node['type'] == 'changed':
        return "Property '{0}{1}' was updated. From {2} to {3}".format(
            parent,
            node['name'],
            stringify(node['value_before']),
            stringify(node['value_after']),
        )


def render(ast, parent):
    """
    Render AST to string.

    Args:
        ast: map
        parent: str

    Returns:
        str
    """
    filtered = filter(lambda node: node['type'] != 'unchanged', ast)
    output = map(
        lambda node: get_action_by_type(node, parent, render),
        filtered,
    )

    return '\n'.join(output)
