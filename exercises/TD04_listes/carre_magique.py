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
    j = 0
    for i in range(0, len(carre)):
        while j != 4:
            somme += int(carre[i][j])
            j += 1
        liste.append(somme)
        j = 0 
        somme = 0

        if (len(set(liste)) == 1):
            return liste[0]
        else:
            return -1


#print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    somme = 0
    liste = []
    j = 0
    for i in range(0, len(carre)):
        while j != 4:
            somme += int(carre[j][i])
            j += 1
        liste.append(somme)
        j = 0 
        somme = 0

    if (len(set(liste)) == 1):
            return liste[0]
        else:
            return -1

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))