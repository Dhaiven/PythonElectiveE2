# Exercice 6.4 Nombre de Harshad

def is_harshad(n):
    """Retourne la vérité de "n est un nombre de Harshad"

    Args:
        n (int): entier à tester

    Returns:
        boolean: True si n est un nombre de Harshad, False sinon

    >>> [ is_harshad(i) for i in [12, 14, 18, 19, 20, 21, 24, 26, 27] ]
    [True, False, True, False, True, True, True, False, True]
    """
    # conversion to string helps for iterating over digits
    # a builtin function may be used to sum elements of a list
    # a one liner solution is possible with list comp
    if not isinstance(n, int):
        return False
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0
