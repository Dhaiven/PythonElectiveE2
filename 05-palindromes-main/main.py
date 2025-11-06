#### Fonction secondaire
def ispalindrome(p):
    return p == p[::-1]

#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()