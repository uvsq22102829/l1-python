import tkinter as tk

ecran = tk.Tk()
ecran.geometry("700x700")


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def cercle(event):
    if event.x > 250:
        cercle_1 = tk.Canvas.create_oval(canvas,(event.x - 50), (event.y - 50),(event.x + 50), (event.y + 50), outline="red") 
    else:
        cercle_1 = tk.Canvas.create_oval(canvas,(event.x - 50), (event.y - 50),(event.x + 50), (event.y + 50), outline="blue") 



def pixel(event):
    r = 255
    g = 0
    b = 0
    color = get_color(r, g, b)
    ligne = tk.Canvas.create_line(canvas, (event.x),(event.y),(event.x + 1),(event.y + 1), fill=color)
    

canvas = tk.Canvas(ecran, height=500, width=500, bg="black")
canvas.grid()

ligne_blanche = tk.Canvas.create_line(canvas, 250, 0, 250, 500, fill="white")

canvas.bind("<Button-3>", pixel)
canvas.bind("<Button-1>", cercle)

ecran.mainloop()