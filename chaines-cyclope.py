def is_cyclope(n):
    """retourne la vérité de "n est un nombre cyclope"

    Args:
        n (int): nombre à tester

    Returns:
        bool: True si "n est un nombre cyclope". False sinon
    
    >>> n = 1230456
    >>> is_cyclope(n)
    True
    >>> n = 1237456
    >>> is_cyclope(n)
    False
    >>> n = 120056
    >>> is_cyclope(n)
    False
    """

    nStr = str(n)
    return len(nStr) % 2 != 0 and nStr[len(nStr)//2] == '0'

def main():
    print(is_cyclope(1230456))
    print(is_cyclope(1237456))
    print(is_cyclope(120056))

if __name__ == "__main__":
    main()
