# Exercice 6.5 Nombre heureux
from unicodedata import digit


def is_happy(n):
    """retourne la vérité de "n est un nombre heureux

    Args:
        n (int): entier à tester

    Returns:
        boolean: True si n est un nombre heureux, False sinon

    >>> [i for i in range(10,40) if is_happy(i) ]
    [10, 13, 19, 23, 28, 31, 32]
    >>> [i for i in range(310,340) if is_happy(i) ]
    [310, 313, 319, 320, 326, 329, 331, 338]
    """
    # think recursive
    # return True for base case
    # return False for base case 
    # conversion to string helps for iterating over digits
    # a builtin function may be used to sum elements of a list

    if not isinstance(n, int):
        return False

    if n == 1:
        return True
    if n == 4:
        return False

    digits = sum(int(d) ** 2 for d in str(n))
    return is_happy(digits)
