import os

# Exercice 6.1 Contenu d'un répertoire

def scand(r):
    """
    Sépare les fichiers et les répertoires du répertoire passé en argument

    Args:
        r: répertoire à analyser

    Returns:
        Liste des noms de fichier sous forme de chaine de caractères
        Liste des noms de répertoire sous forme de chaine de caractères
    >>> f, d = scand('C:\Windows')
    >>> isinstance(f, list) # vrai si f est une liste
    True
    >>> len(f) == 0
    False
    >>> isinstance(d, list) # vrai si d est une liste
    True
    >>> len(d) == 0
    False
    """
    # le contenu des répertoires étant dépendant de la configuration
    # les doctests sont limités
    # créer la liste du contenu du répertoire
    # une list comprehension f pour filtrer les fichiers
    f = [file for file in os.listdir(r) if os.path.isfile(os.path.join(r, file))]
    # une list comprehension d pour filtrer les répertoires
    d = [folder for folder in os.listdir(r) if os.path.isdir(os.path.join(r, folder))]
    return f, d
    


def main():
    # votre code de test ici...
    # Exemple
    # f, d = scand('C:\Windows')
    # print(f)
    # print(d)
    pass

if __name__ == '__main__':
    main()