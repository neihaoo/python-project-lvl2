"""Gendiff AST Module."""


def build_ast_node(key, first_dict, second_dict, function):
    """
    Build node for AST.

    Args:
        key: str
        first_dict: dict
        second_dict: dict
        function: fn

    Returns:
        dict
    """
    first_value = first_dict.get(key)
    second_value = second_dict.get(key)

    if key not in second_dict:
        return {'type': 'deleted', 'name': key, 'value': first_value}
    if key not in first_dict:
        return {'type': 'added', 'name': key, 'value': second_value}
    if isinstance(first_value, dict) and isinstance(second_value, dict):
        return {
            'type': 'nested',
            'name': key,
            'children': function(first_value, second_value),
        }
    if first_value == second_value:
        return {'type': 'unchanged', 'name': key, 'value': first_value}

    return {
        'type': 'changed',
        'name': key,
        'value_before': first_value,
        'value_after': second_value,
    }


def build_ast(first, second):
    """
    Generate diff between two dictionaries.

    Args:
        first: dict
        second: dict

    Returns:
        list
    """
    uniq_keys = sorted(first.keys() | second.keys())

    ast = map(
        lambda key: build_ast_node(key, first, second, build_ast),
        uniq_keys,
    )

    return list(ast)
