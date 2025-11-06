import math

#### Fonction secondaire
def isprime(p):
    for d in range(2, math.ceil(math.sqrt(p)) + 1):
        if p % d == 0:
            return False
    return True

#### Fonction principale
def main():
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
