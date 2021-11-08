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
    
    for ligne in range(-1, -len(carre)):
        colone = -1
        somme_1 += int(carre[ligne][colone])
        colone -= 1
    liste_2.append(somme)
 

    if liste.count(liste[0]) == len(liste) and liste.count(liste_2[0]) == len(liste_2):
        return liste[0]
    else:
        return -1

print(testDiagonalesEgales(carre_mag))
#print(testDiagonalesEgales(carre_pas_mag))