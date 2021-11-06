def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print('   '.join([str(j) for j in i]))


carre_mag = ((4, 14, 15, 1), (9, 7, 6, 12), (5, 11, 10, 8), (16, 2, 3, 13))
carre_pas_mag = ((4, 14, 15, 1), (9, 7, 6, 12), (5, 11, 10, 8), (16, 2, 7, 13))
afficheCarre(carre_mag)
print("")
afficheCarre(carre_pas_mag)
