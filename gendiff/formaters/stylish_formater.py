"""Gendiff Stylish Formater Module."""

import itertools
from typing import List, Union

from gendiff.build_diff_tree import ADDED, CHANGED, DELETED, NESTED, UNCHENGED
from gendiff.formaters.common import get_type_action, transform_value

status_marks = {
    ADDED: '+',
    DELETED: '-',
    UNCHENGED: ' ',
}


def get_diff_node(node, depth, mark, _):
    """Get diff node by mark."""
    return format_node(node['name'], node['value'], depth, status_marks[mark])


def get_changed_node(node, depth, *_):
    """Get changed diff node."""
    return '\n'.join(
        [
            format_node(
                node['name'],
                node['value_before'],
                depth,
                status_marks[DELETED],
            ),
            format_node(
                node['name'],
                node['value_after'],
                depth,
                status_marks[ADDED],
            ),
        ],
    )


def get_nested_node(node, depth, _, function):
    """Get nested diff node."""
    return '  {0}{1}: {2}'.format(
        set_indent(depth),
        node['name'],
        function(node['children'], depth + 2),
    )


types_actions = {
    ADDED: get_diff_node,
    CHANGED: get_changed_node,
    DELETED: get_diff_node,
    NESTED: get_nested_node,
    UNCHENGED: get_diff_node,
}


def set_indent(indent_size: int = 0) -> str:
    """Set indent."""
    return '  ' * indent_size


def stringify(
    node_data: Union[str, int, bool, None, dict],
    indent_size: int,
) -> str:
    """Stringify data."""
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
    """Format data to string."""
    return '{0}{1} {2}: {3}'.format(
        set_indent(indent_size),
        mark,
        node_key,
        stringify(node_value, indent_size),
    )


def render(diff: List[dict], indent_size: int = 0) -> str:
    """Render AST to string."""
    output = map(
        lambda diff_node: get_type_action(types_actions, diff_node['type'])(
            diff_node,
            indent_size,
            diff_node['type'],
            render,
        ),
        diff,
    )

    return '{{\n{0}\n{1}}}'.format(
        '\n'.join(output),
        set_indent(indent_size - 1),
    )
