# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    # Renvoie la valeur en seconde de temps donné jour,heure,minute,secondes
    temps = temps[3] + (temps[2] * 60) + (temps[1] * 60 * 60) + (temps[0] * 24 * 60 * 60)
    return temps

temps = ( 3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    # Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument
         
    seconde = (seconde[0], seconde[1], seconde[2], seconde[3])
    return seconde

temps = secondeEnTemps(100000)
print(temps1[0],"jours",temps1[1],"heures",temps1[2],"minutes",temps1[3],"secondes")
