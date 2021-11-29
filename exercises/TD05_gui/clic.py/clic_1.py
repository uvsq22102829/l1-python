import tkinter as tk

ecran = tk.Tk()
ecran.geometry("700x700")


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def pixel(event):
    r = 255
    g = 0
    b = 0
    color = get_color(r, g, b)
    ligne = tk.Canvas.create_line(canvas,event.x,event.y,(event.x + 1),(event.y + 1), fill=color)
    

canvas = tk.Canvas(ecran, height=500, width=500, bg="black")
canvas.grid()
canvas.bind("<Button-1>", pixel)

ecran.mainloop()