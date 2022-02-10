"""Gendiff Plain Formater Module."""

from typing import Union

from gendiff.formaters.common import transform_value

ADDED = 'added'
CHANGED = 'changed'
DELETED = 'deleted'
NESTED = 'nested'

messages_templates = {
    ADDED: "Property '{0}{1}' was added with value: {2}",
    CHANGED: "Property '{0}{1}' was updated. From {2} to {3}",
    DELETED: "Property '{0}{1}' was removed",
}

types_actions = {
    ADDED: lambda node, parent, _: messages_templates[ADDED].format(
        parent,
        node['name'],
        stringify(node['value']),
    ),
    CHANGED: lambda node, parent, _: messages_templates[CHANGED].format(
        parent,
        node['name'],
        stringify(node['value_before']),
        stringify(node['value_after']),
    ),
    DELETED: lambda node, parent, _: messages_templates[DELETED].format(
        parent,
        node['name'],
    ),
    NESTED: lambda node, parent, function: function(
        node['children'],
        '{0}{1}.'.format(parent, node['name']),
    ),
}


def stringify(node_data: Union[str, int, bool, None, dict]) -> str:
    """
    Stringify data.

    Args:
        node_data: str | int | bool | None | dict

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


def render(ast: list, path: str) -> str:
    """
    Render AST to string.

    Args:
        ast: list
        path: str

    Returns:
        str
    """
    filtered = filter(lambda ast_node: types_actions.get(ast_node['type']), ast)
    output = map(
        lambda ast_node: types_actions[ast_node['type']](
            ast_node,
            path,
            render,
        ),
        filtered,
    )

    return '\n'.join(output)
