"""Manipulation de mots de la langue française"""

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")


def read_data(filename):
    """ Lit les mots contenus dans filname et les retourne sous forme de liste 
    
    Args:
        filename (str): nom du fichier à lire
        
    returns: list of str
    """
    with open(filename, 'r', encoding='utf-8') as f:
        mots = [mot.strip() for mot in f.readlines()]
    return mots


def ensemble_mots(filename):
    """retourne les mots contenus dans filename sous forme d'ensemble
    Args:
        filename (str): mon du fichier
    
    returns:
        set of str
    """
    return set(read_data(filename))


def mots_de_n_lettres(mot, n):
    """retourne le sous ensemble des mots de n lettres
    Args:
      mots (set): Ensemble de mots.
        n (int): Longueur des mots recherchés.

    Returns:
        set: Mots de longueur n.

    """
    return {mot for mot in mot if len(mot) == n}

def mots_avec(mots, s):
    """retourne le sous ensemble des mots incluant la lettre l"""
    return {mot for mot in mots if s in mot}

def cherche1(mots, start, stop, n):
    """retourne le sous ensemble des mots de n lettres commençant par start et finissant par stop"""    
    return {mot for mot in mots if len(mot) == n and mot.startswith(start) and mot.endswith(stop)}


def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    """effectue une recherche complexe dans un ensemble de mots"""
    resultat = set()
    for mot in mots:
        if nmin <= len(mot) <= nmax:
            if any(mot.startswith(start) for start in lstart):
                if any(mid in mot[1:-1] for mid in lmid):
                    if any(mot.endswith(stop) for stop in lstop):
                        resultat.add(mot)
    return resultat


def main():
    """Programme principal"""
    ens = ensemble_mots(FILENAME)
    print(cherche1(ens, 'a','e',5))

if __name__ == "__main__":
    main()
