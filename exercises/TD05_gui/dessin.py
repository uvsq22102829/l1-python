import tkinter as tk
import random

ecran = tk.Tk()
ecran.title("Mon dessin")

ecran.geometry("600x600")
ecran.configure(bg="grey")

color = "blue"
def entrer_couleur():
    global color
    reponse_couleur = input("Entrer une couleur")
    color = reponse_couleur

def undo():
    global objects
    if objects[-1] == Carres:
        canvas.delete(Carres)
    



button_1 = tk.Button(ecran, text="Choisir une couleur", font = ("helvetica", "25"), bg="blue",command=entrer_couleur)
button_1.grid(row=0, column=1, pady=5)



def Carres():
    x0 = random.randint(0, (width-100))
    y0 = random.randint(0, (height-100))
    carre = tk.Canvas.create_rectangle(fond_noir, (x0,y0), ((100 + x0), (100 + y0)), outline=color)
    global objects
    objects.append(carre)
    return carre

def Croixs():
    x0 = random.randint(0, (width-100))
    y0 = random.randint(0, (height-100))
    ligne_1 = tk.Canvas.create_line(fond_noir, (x0, y0), ((x0 + 100), (y0 + 100)), fill=color)
    ligne_2 = tk.Canvas.create_line(fond_noir, ((x0+100), y0), (x0, (y0 + 100)), fill=color)
    global objects
    objects.append(ligne_1) 
    objects.append(ligne_2)
    return ligne_1, ligne_2

def Cercles():
    x0 = random.randint(0, (width-100))
    y0 = random.randint(0, (height-100))
    cercle = tk.Canvas.create_oval(fond_noir, (x0, y0), ((100 + x0), (100 + y0)), outline=color)
    global objects
    objects.append(cercle)
    return cercle
    


button_2 = tk.Button(ecran, text="Cercle", font=("helvetica", "25"), bg="red", fg="white", command=Cercles)
button_2.grid(column=0, row=1, pady=10)

button_3 = tk.Button(ecran, text="Carré", font=("helvetica", "25"), bg="red", fg="white", command=Carres)
button_3.grid(column=0, row=2, pady=10)

button_4 = tk.Button(ecran, text="Croix", font=("helvetica", "25"), bg="red", fg="white", command=Croixs)
button_4.grid(column=0, row=3, pady=10)

button_5 = tk.Button(ecran, text="Undo", font = ("helvetica", "25"), bg="yellow", command=undo)
button_5.grid(row=0, column=2, pady=5, padx=5)
 

fond_noir = tk.Canvas(ecran, bg="black", borderwidth=3, relief="groove", highlightbackground="white")
fond_noir.grid(row=1, rowspan=3, column=1, columnspan=2, padx=5, pady=5)   

# fonction qui permet de connaître les dimensions d'un widget
fond_noir.update()
# Récupére la largeur
width = fond_noir.winfo_width() 
# Récupére la hauteur
height = fond_noir.winfo_height()

objects = []
print(objects)
ecran.mainloop()