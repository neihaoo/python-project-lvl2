"""Gendiff Common Formaters Module."""

from typing import Union


def transform_value(node_value: Union[str, int, bool, None]) -> str:
    """
    Transfom input values to string.

    Args:
        node_value: str | int | bool | None

    Returns:
        str
    """
    if isinstance(node_value, bool):
        return str(node_value).lower()
    if node_value is None:
        return 'null'

    return str(node_value)
