"""Gendiff Common Formaters Module."""

from typing import Union


def transform_value(node_value: Union[str, int, bool, None]) -> str:
    """Transfom input values to string."""
    if isinstance(node_value, bool):
        return str(node_value).lower()
    if node_value is None:
        return 'null'

    return str(node_value)


def get_type_action(actions: dict, node_type: str) -> str:
    """Get action for node by type."""
    return actions.get(node_type)
