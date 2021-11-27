import tkinter as tk


width = input("Entrer la taille du cercle")
nombre_cercle = input("Entrer le nombre de cercle que vous voulez")

ecran = tk.Tk()

ecran.geometry("800x800")
ecran.title("Cible")


color = ["blue", "green", "black", "yellow", "magenta", "red"]
canvas = tk.Canvas(ecran, height=800, width= 800, bg="grey")
canvas.grid()
longueur = 0
a = 0
j = 0

while a != int(nombre_cercle):
        cercle = tk.Canvas.create_oval(canvas, ((0 + longueur), (0 + longueur)), ((int(width) - longueur), (int(width) - longueur)), fill=color[j])
        print(j)
        if j == len(color) - 1:
            j = 0
        j += 1
        longueur += (int(width) // 2) // int(nombre_cercle) 
        a += 1
        


ecran.mainloop() 