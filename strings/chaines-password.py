import string

def check_password(password):
    """
    Teste la robustesse d'un password

    Args:
        password: chaine de caractères

    Returns:
        True or False

    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """

    # Si la longueur n'est pas conforme, retourner False
    # Si l'un des caractères n'est pas un chiffre, retourner False
    # Si l'un des caractères n'est pas une lettre minuscule, retourner False
    # Si l'un des caractères n'est pas une lettre majuscule, retourner False

    # Q : Où puis je trouver l'ensemble des lettres et des chiffres sans le reconstituer moi même ? 
    # R : Jeter un oeil au module string

    if len(password) < 10:
        return False

    hasDigit = False
    for digit in string.digits:
        if digit in password:
            hasDigit = True
            break
    if not hasDigit:
        return False

    hasLowerLetter = False
    for letter in string.ascii_lowercase:
        if letter in password:
            hasLowerLetter = True
            break
    if not hasLowerLetter:
        return False

    hasUpperLetter = False
    for letter in string.ascii_uppercase:
        if letter in password:
            hasUpperLetter = True
            break
    if not hasUpperLetter:
        return False

    return True

def main():
    # Exemple :
    result = check_password('A1213pokl')
    print(result)

if __name__ == '__main__':
    main()