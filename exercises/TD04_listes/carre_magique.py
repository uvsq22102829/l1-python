def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print('   '.join([str(j) for j in i]))


carre_mag = ([4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13])
carre_pas_mag = ([4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13])
#afficheCarre(carre_mag)
#print("")
#afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes
     ont la même somme, et -1 sinon """
    somme = 0
    liste = []
    colone = 0
    for ligne in range(0, len(carre)):
        while colone != 4:
            somme += int(carre[ligne][colone])
            colone += 1
        liste.append(somme)
        colone = 0 
        somme = 0

        
    if liste.count(liste[0]) == len(liste):         
        return liste[0]
    else:
        return -1


#print(testLignesEgales(carre_mag))
#print("")
#print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    somme = 0
    liste = []
    colone = 0
    for ligne in range(0, len(carre)):
        while colone != 4:
            somme += int(carre[colone][ligne])
            colone += 1
        liste.append(somme)
        colone = 0 
        somme = 0

    if liste.count(liste[0]) == len(liste):
        return liste[0]
    else:
        return -1

#print(testColonnesEgales(carre_mag))
#print("")
#print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    somme = 0
    somme_1 = 0
    liste = []
    liste_2 = []
    colone = 0
    for ligne in range(0, len(carre)):
        somme += int(carre[ligne][colone])
        colone += 1
    liste.append(somme)
    colone = -1

    for ligne in range(-1, -len(carre)-1, -1):
        somme_1 += int(carre[ligne][colone])
        colone -= 1

    liste_2.append(somme_1)


    if (liste.count(liste[0]) == len(liste)) and (liste_2.count(liste_2[0]) == len(liste_2)):
        return liste_2[0]
    else:
        return -1

#print(testDiagonalesEgales(carre_mag))
#print(testDiagonalesEgales(carre_pas_mag))



def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if (testLignesEgales(carre) != -1) and (testColonnesEgales(carre) != -1) and (testDiagonalesEgales(carre) != -1):
        print(testLignesEgales(carre), testColonnesEgales(carre), testDiagonalesEgales(carre))
        return True
    else:
        return False

#print(estCarreMagique(carre_mag))
#print(estCarreMagique(carre_pas_mag))



"""9. Un carré d'ordre $n$ est *normal* s'il contient tous les entiers de 1 à $n^2$. 
Ecrire une fonction qui teste si un carré est normal (pas nécessairement magique)."""

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = len(carre)
    dans_la_liste = 0
    liste = []
    print(n)
    for i in range(1, n ^ 2 + 1):
        if i in carre:
            dans_la_liste == 1
            print(dans_la_liste)
            liste.append(dans_la_liste)
            
    print(liste)
    if (liste.count(liste[0]) == len(liste)):
        return True
    else:
        return False



print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))