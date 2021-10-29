def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            liste.append(n)
        else:
            n = n * 3 + 1 
            liste.append(n)
    return liste
        
print(syracuse(6))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, n_max + 1):
        a = syracuse(i)
        if a[-1] != 1:
            return False
    return True

#print(testeConjecture(10000))


""" On appelle *temps de vol* de l’entier `n` le nombre d’étapes pour aller de `n` jusqu’à 1. Le temps de vol de 1 est 0, le temps de vol de 3 est 7. 
Écrire une fonction qui, étant donné un paramètre `n`, renvoie son temps de vol."""

def tempsVol(n):
    """ Retourne le temps de vol de n """
    suite_syracuse = syracuse(n)
    temps_vol = len(suite_syracuse)
    return temps_vol

print("Le temps de vol de", 6, "est", tempsVol(6))

"""5. Ecrire une fonction qui, étant donné un paramètre `n_max` renvoie la liste 
des temps de vol de tous 
les entiers de 1 à `n_max`. *Indication*: utiliser une liste en compréhension."""

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste_temps_vol = []
    for i in range(1, n_max + 1):
        a = print(tempsVol(i))
        liste_temps_vol.append(a)

print(tempsVolListe(100))