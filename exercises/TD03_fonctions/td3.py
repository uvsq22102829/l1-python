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
    seconde = (jour, heure, minute, secondes)  
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
#afficheTemps((1,0,14,23))  


# def qui va demander à l'utilisateur d'entrée un temps. 
def demandeTemps():
    j = 0
    temps = []
    while j != 4:
        reponse_utilisateur = int(input(f"Entrer un nombre de {liste[j]}"))
        if j == 1 and (reponse_utilisateur > 24 or reponse_utilisateur < 0):
            while int(reponse_utilisateur) > 24 or int(reponse_utilisateur) < 0:
                reponse_utilisateur = input(f"Pas une valeur correctre. Entrer un nombre de {liste_1[j]} compris entre 0 et 24 ")   

        elif j == 2 and (reponse_utilisateur > 60 or reponse_utilisateur < 0):
            while int(reponse_utilisateur) > 60 or int(reponse_utilisateur) < 0:
                reponse_utilisateur = input(f"Pas une valeur correctre. Entrer un nombre de {liste_1[j]} compris entre 0 et 60 ")

        elif j == 3 and (reponse_utilisateur > 60 or reponse_utilisateur < 0):
            while int(reponse_utilisateur) > 60 or int(reponse_utilisateur) < 0:
                reponse_utilisateur = input(f"Pas une valeur correctre. Entrer un nombre de {liste_1[j]} compris entre 0 et 60 ")
        j += 1
        temps.append(reponse_utilisateur)
    return temps
        

liste_1 = ["jour(s)", "heure(s)", "minute(s)", "seconde(s)"]
#afficheTemps(demandeTemps())



# def qui va faire la somme de deux temps
def sommeTemps(temps1, temps2):
    somme_temps = []
    k = 0
    while k != 4:
        somme = temps1[k] + temps2[k]
        somme_temps.append(somme)
        k += 1
    afficheTemps(somme_temps)
    return somme_temps
    
#sommeTemps((2,3,4,25),(5,22,57,1))


# def qui va calculer un pourcentage d'un temps. 
def proportionTemps(temps, proportion):
    temps = tempsEnSeconde(temps)
    print(temps)
    temps = proportion * temps
    temps = secondeEnTemps(temps)
    return temps


#afficheTemps(proportionTemps((2,0,36,0),0.2))


"""On veut maintenant afficher un temps sous forme de date, en supposant 
que le temps 0 est le 1 janvier 1970 à 00:00:00.

* Implémenter une fonction `tempsEnDate`qui donne la date sous
 la forme (année, jour, heure, minute, seconde).
* Implémenter la fonction `afficheDate`qui affiche la date. 
"""

def tempsEnDate(temps):

    afficheTemps(temps)
    while int(temps[0]) >= 365:
        if int(temps[0]) >= 365:
            annee = +1
    liste = liste[i].insert(0,"annee")
    date = temps.insert(0,annee)
    return date
    

        

def afficheDate(date = -1):
    pass
    
temps = secondeEnTemps(1000000000)
tempsEnDate(temps)
#afficheDate(tempsEnDate(temps))
#afficheDate()