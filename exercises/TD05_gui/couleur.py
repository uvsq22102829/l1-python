import tkinter as tk
import random

ecran = tk.Tk()
ecran.geometry("600x500")

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    canvas_2 = tk.Canvas.create_line(canvas, i, j, i, j, fill=color)
    

def ecran_aleatoire():
    a = 0
    i = 0
    j = 0
    while a != (256 * 256):
        while i != 256:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = get_color(r, g, b)
            draw_pixel(i, j, color)
            i += 1
            print(a)
            a += 1
        i = 0
        j +=1

    



button_1 = tk.Button(ecran, text="Aléatoire", fg="blue", bg="white", font=(20), command=ecran_aleatoire)
button_1.grid(row = 0, column=0, pady=20)

button_2 = tk.Button(ecran, text="Dégradé gris", fg="blue", bg="white", font=20)
button_2.grid(row = 1, column= 0, pady=20)

button_3 = tk.Button(ecran, text="Dégradé 2D", fg="blue", bg="white", font=20)
button_3.grid(row = 2, column= 0, pady=20)

canvas = tk.Canvas(ecran, bg="black", height= 256, width=256)
canvas.grid(column = 1, row= 0, rowspan=3)

draw_pixel(128, 128, (get_color(255,255,255)))

ecran.mainloop()