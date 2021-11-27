import tkinter as tk

ecran = tk.Tk()
ecran.geometry("600x500")

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    

draw_pixel((256//2),(256//2), "white")

button_1 = tk.Button(ecran, text="Aléatoire", fg="blue", bg="white", font=(20))
button_1.grid(row = 0, column=0, pady=20)

button_2 = tk.Button(ecran, text="Dégradé gris", fg="blue", bg="white", font=20)
button_2.grid(row = 1, column= 0, pady=20)

button_3 = tk.Button(ecran, text="Dégradé 2D", fg="blue", bg="white", font=20)
button_3.grid(row = 2, column= 0, pady=20)

canvas = tk.Canvas(ecran, bg="black", height= 256, width=256)
canvas.grid(column=1, row= 0, rowspan=3)

ecran.mainloop()