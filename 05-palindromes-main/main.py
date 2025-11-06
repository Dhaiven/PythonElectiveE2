#### Fonction secondaire
def ispalindrome(p):
    middle = len(p) // 2
    return p[:middle] == p[-1: middle : -1]

#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()