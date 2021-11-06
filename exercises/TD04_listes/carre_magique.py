def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print('   '.join([str(j) for j in i]))


carre_mag = ((4, 14, 15, 1), (9, 7, 6, 12), (5, 11, 10, 8), (16, 2, 3, 13))
carre_pas_mag = ((4, 14, 15, 1), (9, 7, 6, 12), (5, 11, 10, 8), (16, 2, 7, 13))
#afficheCarre(carre_mag)
#print("")
#afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes
     ont la même somme, et -1 sinon """
    somme = 0
    liste = []
    for i in range(0, len(carre)):
        for j in range(0, len(carre)):
            somme += int(carre[j][i])
        liste.append(somme)
        print(somme)
    for k in range(0, len(liste)):
        if liste[k] == liste[k + 1]:
            return somme
        else:
            return - 1
            

print(testLignesEgales(carre_mag))
#print(testLignesEgales(carre_pas_mag))
