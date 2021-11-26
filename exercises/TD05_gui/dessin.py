import tkinter as tk

ecran = tk.Tk()
ecran.title("Mon dessin")

ecran.geometry("900x700")
ecran.configure(bg="grey")
button_1 = tk.Button(ecran, text="Choisir une couleur", font = ("helvetica", "25"), bg="blue")
button_1.grid(row=0, column=1,columnspan=3)

button_2 = tk.Button(ecran, text="Cercle", font = ("helvetica", "25"), bg="black", fg="white")
button_2.grid(column=0, row=1, pady=20)

button_3 = tk.Button(ecran, text="Carré", font = ("helvetica", "25"), bg="black", fg="white")
button_3.grid(column=0, row=2, pady=20)

button_4 = tk.Button(ecran, text="Croix", font = ("helvetica", "25"), bg="black", fg="white")
button_4.grid(column=0, row=3, pady=20)

fond_noir = tk.Canvas(ecran, bg = 'black')
fond_noir.grid(row=1, rowspan=4, column=1, columnspan=2, padx=5)   




ecran.mainloop()