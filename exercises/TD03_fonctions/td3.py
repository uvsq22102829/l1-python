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


""" Créer une fonction d'affichage d'un temps `afficheTemps`. Attention, les mots jour, 
heure et seconde doivent être au pluriel s'il y en a plusieurs. S'il y en a zéro, 
ils ne doivent pas apparaître.
`print(message, end="")` permet de ne pas sauter une ligne après un print. 
Vous pouvez écrire une fonction qui affiche un mot au pluriel ou non, appelée 
ensuite plusieurs fois par `afficheTemps` pour simplifier votre code.
"""

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
afficheTemps((1,0,14,23))  