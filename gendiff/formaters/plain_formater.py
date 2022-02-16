"""Gendiff Plain Formater Module."""

from typing import Callable, List, Union

from gendiff.build_diff_tree import ADDED, CHANGED, DELETED, NESTED
from gendiff.formaters.common import get_type_action, transform_value

messages_templates = {
    ADDED: "Property '{0}{1}' was added with value: {2}",
    CHANGED: "Property '{0}{1}' was updated. From {2} to {3}",
    DELETED: "Property '{0}{1}' was removed",
}


def get_added_message(node: dict, parent: str, _) -> str:
    """Get string for added node."""
    return messages_templates[ADDED].format(
        parent,
        node['name'],
        stringify(node['value']),
    )


def get_changed_message(node: dict, parent: str, _) -> str:
    """Get string for changed node."""
    return messages_templates[CHANGED].format(
        parent,
        node['name'],
        stringify(node['value_before']),
        stringify(node['value_after']),
    )


def get_deleted_message(node: dict, parent: str, _) -> str:
    """Get string for deleted node."""
    return messages_templates[DELETED].format(
        parent,
        node['name'],
    )


def get_nested_message(
    node: dict,
    parent: str,
    function: Callable[[List[dict], str], str],
) -> str:
    """Get string for nested node."""
    return function(node['children'], '{0}{1}.'.format(parent, node['name']))


types_actions = {
    ADDED: get_added_message,
    CHANGED: get_changed_message,
    DELETED: get_deleted_message,
    NESTED: get_nested_message,
}


def stringify(node_data: Union[str, int, bool, None, dict]) -> str:
    """Stringify data."""
    if isinstance(node_data, str):
        return "'{0}'".format(node_data)

    return (
        '[complex value]'
        if isinstance(node_data, dict)
        else transform_value(node_data)
    )


def render(tree: List[dict]) -> str:
    """Render diff to string."""

    def walk(diff_tree: List[dict], path: str) -> str:
        filtered = filter(
            lambda diff_node: get_type_action(types_actions, diff_node['type']),
            diff_tree,
        )
        output = map(
            lambda diff_node: get_type_action(types_actions, diff_node['type'])(
                diff_node,
                path,
                walk,
            ),
            filtered,
        )

        return '\n'.join(output)

    return walk(tree, '')
