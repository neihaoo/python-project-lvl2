"""Gendiff Common Formaters Module."""


def transform_value(node_value):
    """
    Transfom boolen and None values to string.

    Args:
        node_value: any

    Returns:
        str
    """
    if isinstance(node_value, bool):
        return str(node_value).lower()
    if node_value is None:
        return 'null'

    return str(node_value)
