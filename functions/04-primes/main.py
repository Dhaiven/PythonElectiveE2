import math

#### Fonction secondaire
def isprime(p):
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    limit = int(math.sqrt(p)) + 1
    for d in range(3, limit, 2):
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