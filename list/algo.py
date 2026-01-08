def min(l: list) -> int:
    """Retourne le minimum d'une liste de nombres
    >>> l = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> min(l)
    15
    """
    k = 1
    i = 0
    while k < len(l):
        if l[k] < l[i]:
            i = k
        k += 1
    return l[i]


def max(l: list) -> int:
    """Retourne le maximum d'une liste
    >>> l = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> max(l)
    49
    """
    k = 1
    i = 0
    while k < len(l):
        if l[k] > l[i]:
            i = k
        k += 1
    return l[i]


def ind_mini(l: list) -> int:
    """Retourne l'indice minimum d'une liste
    >>> l = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> ind_mini(l)
    3
    """
    k = 1
    i = 0
    while k < len(l):
        if l[k] < l[i]:
            i = k
        k += 1
    return i


def ind_maxi(l: list):
    """Retourne l'indice maximal d'une liste
    >>> l = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> ind_maxi(l)
    8
    """
    k = 1
    i = 0
    while k < len(l):
        if l[k] > l[i]:
            i = k
        k += 1
    return i


def somme(l: list):
    """Retourne la somme d'une liste de nombres
    >>> l = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> somme(l)
    337
    """
    k = 0
    result = 0
    while k < len(l):
        result += l[k]
        k += 1
    return result


def moyenne(l: list):
    """Retourne la moyenne d'une liste de nombres
    >>> l = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> moyenne(l)
    33.7
    """
    return somme(l) / len(l)


def est_trie(l: list):
    """Retourne la moyenne d'une liste de nombres

    Args:
        l: liste de nombres

    Returns:
        - 1 si la liste est triée dans l'ordre croissant
        - -1 si la liste est triée dans l'ordre décroissant
        - 0 sinon
    >>> l = [33, 36, 27, 15, 43, 35, 36, 42, 49, 21]
    >>> est_trie(l)
    0
    >>> l = [15, 21, 27, 33, 35, 36, 36, 42, 43, 49]
    >>> est_trie(l)
    1
    >>> l = [49, 43, 42, 36, 36, 35, 33, 27, 21, 15]
    >>> est_trie(l)
    -1
    """
    if len(l) < 2: return 1

    croissant = True
    decroissant = True

    for k in range(len(l) - 1):
        if l[k] > l[k + 1]: croissant = False
        if l[k] < l[k + 1]: decroissant = False

    if croissant: return 1
    if decroissant: return -1
    return 0

def doublons(l: list) -> list:
    """Retourne la liste des doublons dans une liste
    >>> l = [2, 1, 1, 3, 4, 4]
    >>> doublons(l)
    [1, 4]
    """
    k = 0
    result = []
    while k < len(l):
        for j in range(k + 1, len(l)):
            if l[k] == l[j] and l[k] not in result:
                result.append(l[k])
        k += 1
    return result


def elts_communs(l1: list, l2: list) -> list:
    """Retourne la liste des doublons dans une liste

    Args:
        l1: liste de nombres
        l2: liste de nombres

    Returns:
        La liste des doublons
    >>> elts_communs([2, 1, 1, 3, 4, 4], [5, 4, 3, 2, 1])
    [2, 1, 3, 4]
    """
    k = 0
    result = []
    while k < len(l1):
        if l1[k] not in result and l1[k] in l2:
            result.append(l1[k])
        k += 1
    return result


def elts_differents(l1: list, l2: list) -> list:
    """Retourne la liste des éléments différents dans une liste

    Args:
        l1: liste de nombres
        l2: liste de nombres

    Returns:
        La liste des éléments différents
    >>> elts_differents([2, 1, 1, 3, 4, 4], [5, 4, 3, 2, 1])
    []
    """
    k = 0
    result = []
    while k < len(l1):
        if l1[k] not in result and l1[k] not in l2:
            result.append(l1[k])
        k += 1
    return result

# TODO: finish + tests

def main():
    liste = [5, 3, 6, 2, 10, 4]
    print("La liste est :", liste)
    print("Le minimum est :", min(liste))

if __name__ == "__main__":
    main()