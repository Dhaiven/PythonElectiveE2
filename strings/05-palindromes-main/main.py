import unicodedata

#### Fonction secondaire
def ispalindrome(p):
    """
    Vérifie si une chaîne est un palindrome en ignorant la casse,
    les accents, les espaces et la ponctuation.

    >>> ispalindrome("L'âme sûre ruse mal")
    True
    >>> ispalindrome("Radar")
    True
    """
    p = p.casefold()
    p = unicodedata.normalize("NFKD", p)
    p = "".join(ch for ch in p if not unicodedata.combining(ch))
    p = "".join(ch for ch in p if ch.isalnum())
    return p == p[::-1]

#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()