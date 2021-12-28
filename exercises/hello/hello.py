import random

def supprime_max_min(l):
    maximum = max(l)
    minimum = min(l)
    l.remove(maximum)
    l.remove(minimum)
    return l

print(supprime_max_min([2, 4, 6, 10]))



def plan_jour(liste):
    n = random.randint(0, 3)
    liste.append(n)
    return liste


def plan_semaine(liste_semaine):
    i = 0
    b = 0
    while i != 7:
        b = plan_jour(liste)
        liste_semaine.append(b)
        i += 1
    return liste_semaine
    
def affiche():
    return plan_semaine(liste_semaine)

liste = []
liste_semaine = []
print(plan_jour(liste))
#print(affiche())


