from tkinter import *


def ver():
    pass


windows = Tk()
windows.geometry("500x200")
menu = Menu(windows)

menudep1 = Menu(menu, tearoff=0)
menudep1.add_command(label="Piso 1", command=ver)
submenu = Menu(menu)
submenu.add_command(label="Habitacion 1")
submenu.add_command(label="Habitacion 2")
submenu.add_command(label="Habitacion 3")
menudep1.add_cascade(label="Piso 2", menu=submenu)
menudep1.add_command(label="Piso 3", command=ver)
menu.add_cascade(label="Edificio 1", menu=menudep1)




windows.config(menu=menu)
mainloop()
