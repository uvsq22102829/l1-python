# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    # Renvoie la valeur en seconde de temps donné jour,heure,minute,secondes
    temps = temps[3] + (temps[2] * 60) + (temps[1] * 3600) + (temps[0] * (24 * 3600))
    return temps


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))   


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

temps = secondeEnTemps(100000)
print(temps[0],"jours", temps[1] ,"heures", temps[2] ,"minutes", temps[3] ,"secondes")
