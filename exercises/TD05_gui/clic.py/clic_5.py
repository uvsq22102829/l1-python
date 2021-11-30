import tkinter as tk

ecran = tk.Tk()
ecran.geometry("700x700")


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def cercle(event):
    global cpt_rouge
    global cpt_bleue
    global liste
    global liste_1
    if event.x > 250:
        liste.append(event.x)
        liste.append(event.y)
        cercle_1 = tk.Canvas.create_oval(canvas, (event.x - 50), (event.y - 50), (event.x + 50), (event.y + 50), outline="red") 
        cpt_rouge += 1
    
        if cpt_rouge == 2:
            ligne_rouge = tk.Canvas.create_line(canvas, liste[0], liste[1], liste[2], liste[3], fill="red")
            cpt_rouge = 0
            liste.clear()
              
    else:
        liste_1.append(event.x)
        liste_1.append(event.y)
        cercle_1 = tk.Canvas.create_oval(canvas, (event.x - 50), (event.y - 50),(event.x + 50), (event.y + 50), outline="blue") 
        cpt_bleue += 1

        if cpt_bleue == 2:
            ligne_bleue = tk.Canvas.create_line(canvas, liste_1[0], liste_1[1], liste_1[2], liste_1[3], fill="blue")
            cpt_bleue = 0
            liste_1.clear()

def forme_aleatoire(event):
    global clique
    clique += 1
    if clique == 10:
        ecran.destroy()
    if (clique % 2) != 0:
        canvas.itemconfigure(carre, fill="grey") 
    else:
        canvas.itemconfigure(carre, fill="white") 


def pixel(event):
    r = 255
    g = 0
    b = 0
    color = get_color(r, g, b)
    ligne = tk.Canvas.create_line(canvas, (event.x),(event.y), (event.x + 1), (event.y + 1), fill=color)
    

def cercle_couleur(event):
    global clique
    global liste
    clique += 1
    for i in range(0, 9):
        cercle_rouge = tk.Canvas.create_oval(canvas, (event.x - 50), (event.y - 50),(event.x + 50), (event.y + 50), outline="red")
        liste.append(cercle_rouge)


    if clique == 9:
        for item in canvas.find_all():
            if canvas.type(item) == 'oval':
                canvas.itemconfig(item, outline='yellow')
        #for i in range(0, 9):
        #canvas.itemconfig(liste[i], outline="yellow")
         
    elif clique == 10:
        for item in canvas.find_all():
            if canvas.type(item) == 'oval':
                canvas.delete(item)
                clique = 0
        #for i in range(0, 9):
         #   canvas.delete(liste[i])
         #   clique = 0
        


canvas = tk.Canvas(ecran, height=500, width=500, bg="black")
canvas.grid()

#carre = tk.Canvas.create_rectangle(canvas, 100, 100, 400, 400, fill="white")

#ligne_blanche = tk.Canvas.create_line(canvas, 250, 0, 250, 500, fill="white")
#canvas.bind("<Button>", forme_aleatoire)
#canvas.bind("<Button-3>", pixel)
#canvas.bind("<Button-1>", cercle)
canvas.bind("<Button>", cercle_couleur)

cpt_bleue = 0
cpt_rouge = 0
clique = 0
liste = []
liste_1 = []

ecran.mainloop()