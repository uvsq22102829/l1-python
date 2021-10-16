# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    # Renvoie la valeur en seconde de temps donné jour,heure,minute,secondes
    temps = temps[3] + (temps[2] * 60) + (temps[1] * 3600) + (temps[0] * (24 * 3600))
    return temps


temps = (3, 23, 1, 34)
# print(type(temps))
# print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):

    # Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument
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



# fonction qui va afficher d'un temps

def afficheTemps(temps):
    for i in range(0, len(temps)):
        if temps[i] >= 1 and temps[i] != 0:
            if temps[i] == 1:
                a = liste[i] + " : " + str(temps[i])
            else:
                a = liste[i] + s + " : " + str(temps[i])
            
            # end = "" permet de ne pas sauter de ligne après print
            print(a, end=" ")
                
   
s = "s"
liste = ["jour", "heure", "minute", "seconde"]
# afficheTemps((1,0,14,23))  



"""Ecrire une fonction qui demande à l'utilisateur de rentrer un nombre de jours, d'heures, de minutes et
de secondes et qui renvoie un temps. Attention, si l'entrée utilisateur n'est pas correcte, par exemple 80 minutes,
afficher un message d'erreur et s'arrêter.

(Optionnel) Au lieu d'arêter le programme, demander de rentrer une nouvelle valeur, tant que 
ce n'est pas une valeur correcte."""

def demandeTemps():
    i 
    while i != 4:
        reponse_utilisateur = input("Entrer un nombre de {liste[i]}")
        i += 1

i = 0
liste = ["jour", "heure", "minute", "seconde"]
afficheTemps(demandeTemps())


