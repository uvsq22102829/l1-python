import tkinter as tk


width = input("Entrer la taille du cercle")
nombre_cercle = input("Entrer le nombre de cercle que vous voulez")

ecran = tk.Tk()

ecran.geometry("800x800")
ecran.title("Cible")


color = ["blue", "green", "black", "yellow", "magenta", "red"]
canvas = tk.Canvas(ecran, height=800, width= 800, bg="black")
canvas.grid()
longueur = 0
j = 0
for i in range(0, len(nombre_cercle) + 1):
    cercle = tk.Canvas.create_oval(canvas, ((0 + longueur), (0 + longueur)), ((int(width) - longueur), (int(width) - longueur)), fill=color[j])
    if j == len(color):
        j = 0
    j += 1
    longueur += int(width) // int(nombre_cercle) 
    print(longueur)
    print(i)

ecran.mainloop() 