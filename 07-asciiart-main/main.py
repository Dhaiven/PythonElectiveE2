#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    C = [s[0]]
    O = [1]
    for k in range(1, len(s)):
        if s[k - 1] == s[k]:
            O[-1] += 1
        else:
            C.append(s[k])
            O.append(1)

    return zip(C, O)


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    identique = 1
    k = 1
    while k < len(s) and s[k] == s[0]:
        identique += 1
        k += 1

    if identique == len(s):
        return [(s[0], identique)]

    return [(s[0], identique)] + artcode_r(s[identique:])
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
