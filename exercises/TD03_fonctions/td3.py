import time


# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
# Renvoie la valeur en seconde de temps donné jour,heure,minute,secondes
def tempsEnSeconde(temps):
    temps = temps[3] + (temps[2] * 60) + (temps[1] * 3600) + (temps[0] * (24 * 3600))
    return temps


temps = (3, 23, 1, 34)


# print(type(temps))
# print(tempsEnSeconde(temps))

# Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument
def secondeEnTemps(seconde):
    jour = seconde // (3600 * 24)
    reste_tps = seconde % (3600 * 24)

    heure = reste_tps // 3600
    reste_tps = reste_tps % 3600

    minute = reste_tps // 60
    reste_tps = reste_tps % 60

    secondes = reste_tps
    seconde = [jour, heure, minute, secondes]
    return seconde


# temps = secondeEnTemps(100000)
# print(f"{temps[0]} jour, {temps[1]} heures, {temps[2]}  minutes, {temps[3]} secondes")


# fonction qui va afficher un temps(jour, heure, minute, seconde)

def afficheTemps(temps):
    for i in range(0, len(temps)):
        if int(temps[i]) >= 1 and int(temps[i]) != 0:
            if temps[i] == 1:
                a = liste[i] + " : " + str(temps[i])
            else:
                a = liste[i] + s + " : " + str(temps[i])

            # end = "" permet de ne pas sauter de ligne après print
            print(a, end=" ")


s = "s"
liste = ["jour", "heure", "minute", "seconde"]


# afficheTemps((1,0,14,23))


# def qui va demander à l'utilisateur d'entrée un temps.
def demandeTemps():
    j = 0
    temps = []
    while j != 4:
        reponse_utilisateur = int(input(f"Entrer un nombre de {liste[j]}"))
        if j == 1 and (reponse_utilisateur > 24 or reponse_utilisateur < 0):
            while int(reponse_utilisateur) > 24 or int(reponse_utilisateur) < 0:
                reponse_utilisateur = input(
                    f"Pas une valeur correctre. Entrer un nombre de {liste_1[j]} compris entre 0 et 24 ")

        elif j == 2 and (reponse_utilisateur > 60 or reponse_utilisateur < 0):
            while int(reponse_utilisateur) > 60 or int(reponse_utilisateur) < 0:
                reponse_utilisateur = input(
                    f"Pas une valeur correctre. Entrer un nombre de {liste_1[j]} compris entre 0 et 60 ")

        elif j == 3 and (reponse_utilisateur > 60 or reponse_utilisateur < 0):
            while int(reponse_utilisateur) > 60 or int(reponse_utilisateur) < 0:
                reponse_utilisateur = input(
                    f"Pas une valeur correctre. Entrer un nombre de {liste_1[j]} compris entre 0 et 60 ")
        j += 1
        temps.append(reponse_utilisateur)
    return temps


liste_1 = ["jour(s)", "heure(s)", "minute(s)", "seconde(s)"]


# afficheTemps(demandeTemps())


# def qui va faire la somme de deux temps
def sommeTemps(temps1, temps2):
    somme_temps = []
    k = 0
    while k != 4:
        somme = temps1[k] + temps2[k]
        somme_temps.append(somme)
        k += 1
    while int(somme_temps[3]) > 60:
        somme_temps[3] -= 60
        somme_temps[2] += 1

    while int(somme_temps[2]) > 60:
        somme_temps[2] -= 60
        somme_temps[1] += 1

    while int(somme_temps[1]) > 24:
        somme_temps[1] -= 24
        somme_temps[0] += 1

    afficheTemps(somme_temps)
    return somme_temps


# sommeTemps((2,3,4,25),(5,22,57,1))


# def qui va calculer un pourcentage d'un temps.
def proportionTemps(temps, proportion):
    temps = tempsEnSeconde(temps)
    temps = proportion * temps
    temps = secondeEnTemps(temps)
    return temps


# afficheTemps(proportionTemps((2,0,36,0),0.2))


def tempsEnDate(temps):
    temps_0 = [1970, 1, 0, 0, 0]
    annee = 0
    while temps[0] >= 365:
        if temps[0] >= 365:
            temps[0] -= 365
            annee += 1

    annee += 1970
    temps.insert(0, annee)

    while int(temps[3]) > 60:
        temps[3] -= 60
        temps[2] += 1

    while int(temps[2]) > 60:
        temps[2] -= 60
        temps[1] += 1

    while int(temps[1]) > 24:
        temps[1] -= 24
        temps[0] += 1
    print(temps)
    return temps


def afficheDate(date=-1):
    date = print(f"{temps[1]} {temps[0]}, ({temps[2]} : {temps[3]} : {temps[4]})")
    return date


liste_2 = ["annee", "jour", "heure", "minute", "seconde"]


# temps = secondeEnTemps(1000000000)
# afficheTemps(temps)
# tempsEnDate(temps)
# afficheDate(tempsEnDate(temps))
# afficheDate()


def bisextile(jour):
    annee = 0
    while jour >= 365:
        if annee % 4 == 0:
            jour -= 366
            annee += 1
        else:
            jour -= 365
            annee += 1
    print(f"Le nombre d'année bissextile depuis le 1 er janvier 2020 est de {annee}")


# bisextile(20000)

"""Implémenter une fonction `nombreBisextile` qui calcule le nombre d'années bisextiles 
pour un nombre de jour donnés pour corriger votre fonction de calcul de la date."""


def nombreBisextile(jour):
    annee_bissextile = 0
    annee_bissextile_jour = 365 * 4 + 1
    i = 0
    while jour >= annee_bissextile_jour:
        if jour >= annee_bissextile_jour:
            jour -= annee_bissextile_jour
            annee_bissextile += 1
            i += 1
    print(annee_bissextile)
    return annee_bissextile


# nombreBisextile(1461)

def tempsEnDateBisextile(temps):
    jour = temps[0]
    print(jour)
    nbr_annee = nombreBisextile(jour)
    temps[0] += nbr_annee
    temps = tempsEnDate(temps)
    return temps


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))