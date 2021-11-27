import tkinter as tk


ecran = tk.Tk()

ecran.geometry("800x800")


color = ["blue", "green", "black", "yellow", "magenta", "red"]

canvas = tk.Canvas(ecran, height="800", width="800") 
canvas.grid()
cercle = tk.Canvas.create_oval(canvas, (0,0), (800,800), overline=color[0])

ecran.mainloop()

