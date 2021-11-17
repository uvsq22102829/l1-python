import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH 
y = CANVAS_HEIGHT 
y1 = CANVAS_HEIGHT 
canvas.create_line(x0, y - 525, x0, y1 - 200)
canvas.create_oval(x0 - 50, y - 575, x1 - 650, y1 - 475)
canvas.create_oval(x0 - 50, (y - 525) * 2 + 25, x1 - 650, (y1 - 475) * 2 + 25)
canvas.create_oval(x0 - 50, y - 165, x1 - 650, y1 - 265)


    
# Fin de votre code

canvas.grid()
root.mainloop()
