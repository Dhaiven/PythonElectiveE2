# import de searchext

def searchext_unique(l):
    """
    Identifie les extensions de la liste de fichiers passée en argument

    Args:
        l : liste des noms de fichier sous forme de chaine de caractères

    Returns:
        Liste des extensions sous forme de chaine de caractères
        
    >>> s = searchext_unique(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(s, set) # vrai si s est un set
    True
    >>> print(sorted(list(s)))
    ['bin', 'exe', 'pif', 'xml']
    >>> s = searchext_unique(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(s, set) # vrai si s est un set
    True
    >>> print(sorted(list(s)))
    ['exe', 'ini', 'log']
    >>> s = searchext_unique(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(s, set) # vrai si s est un set
    True
    >>> print(sorted(list(s)))
    ['exe', 'ini', 'log']
    """

    return set([file.lower().split(".")[-1] for file in l if "." in file])
    
def main():
    s = searchext_unique(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    print(s)
    
if __name__ == "__main__":
    main()