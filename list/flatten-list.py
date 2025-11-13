def flatten_list(l: list)-> list:
    """Aplati une liste de listes en une seule liste

    Args:
        l (list): liste de listes

    Returns:
        list: liste aplatie

    >>> flatten_list([[1, 2, 3], [4, 5], [6]])
    [1, 2, 3, 4, 5, 6]
    >>> flatten_list([['a', 'b'], ['c', 'd', 'e'], ['f']])
    ['a', 'b', 'c', 'd', 'e', 'f']
    >>> flatten_list([[True, False], [False, True]])
    [True, False, False, True]
    """

    result = []
    for value in l:
        if isinstance(value, list):
            result.extend(flatten_list(value))
        else:
            result.append(value)
    return result
