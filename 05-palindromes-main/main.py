#### Fonction secondaire
def ispalindrome(p):
    p = p.casefold()
    p = unicodedata.normalize("NFKD", p)
    p = "".join(ch for ch in p if not unicodedata.combining(ch))
    return p == p[::-1]

#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()