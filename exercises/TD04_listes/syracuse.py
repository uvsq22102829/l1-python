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
        
#print(syracuse(6))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, n_max + 1):
        a = syracuse(i)
        if a[-1] != 1:
            return False
    return True

#print(testeConjecture(10000))



def tempsVol(n):
    """ Retourne le temps de vol de n """
    suite_syracuse = syracuse(n)
    temps_vol = len(suite_syracuse)
    return temps_vol

#print("Le temps de vol de", 6, "est", tempsVol(6))

"""Fonction qui, étant donné un paramètre `n_max` renvoie la liste |
des temps de vol de tous les entiers de 1 à `n_max`."""

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste_temps_vol = []
    for i in range(1, n_max + 1):
        a = tempsVol(i)
        liste_temps_vol.append(a)
        

    #max_val = max(liste_temps_vol) 
    #print(liste_temps_vol.index(max(liste_temps_vol)))
    
    return liste_temps_vol

#print(tempsVolListe(10000))


def max_altitude(n):
    liste = []
    for i in range(1, n + 1):
        liste_syracuse = syracuse(i)
        max_val = max(liste_syracuse)
        liste.append(max_val)
  
    val_max = max(liste)
    return val_max

#print(max_altitude(10000))

