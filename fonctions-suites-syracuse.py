def syracuse(n):
    # initialisation des variables

    start = n
    # tant que la suite n'est pas terminée :
    #   - calcul du n suivant
    #   - mise à jour du temps de vol (tv)
    #   - mise à jour du temps de vol en altitude (tva) si nécessaire
    #   - mise à jour de l'altitude maximale (am)

    tv, tva, am = 0, None, 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if tva is None and n < start:
            tva = tv
        tv += 1
        if n > am:
            am = n

    return tv, tva, am


def main():
    # exemple d'exécution
    n = 15
    tv, tva, am = syracuse(n)
    print(n, tv, tva, am)

    n = 127
    tv, tva, am = syracuse(n)
    print(n, tv, tva, am)

if __name__ == "__main__":
    main()