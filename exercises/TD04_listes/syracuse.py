def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    print(liste)
    while n != 1:
        if n % 2 == 0:
            n //= 2
            liste.append(n)
        else:
            n = n * 3 + 1 
            liste.append(n)
    print(liste)
        

print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    pass

#print(testeConjecture(10000))