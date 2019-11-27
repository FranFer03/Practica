from tkinter import *


def ver():
    pass


windows = Tk()
windows.geometry("500x200")
windows.title("TECNO")
menu = Menu(windows)

tv = Menu(menu, tearoff=0)
submenu_0 = Menu(menu)
submenu_0.add_command(label="Full HD")
submenu_0.add_command(label="4k")
submenu_0.add_command(label="Smart TV")
tv.add_cascade(label="Tipo", menu=submenu_0)
submenu_1 = Menu(menu)
submenu_1.add_command(label="Samsung")
submenu_1.add_command(label="LG")
submenu_1.add_command(label="TCL")
tv.add_cascade(label="MARCA", menu=submenu_1)
submenu_2 = Menu(menu)
submenu_2.add_command(label="23")
submenu_2.add_command(label="46")
submenu_2.add_command(label="55")
tv.add_cascade(label="Pulgadas", menu=submenu_2)
menu.add_cascade(label="TV", menu=tv)

phone = Menu(menu, tearoff=0)
submenu_3 = Menu(menu)
submenu_3.add_command(label="Samsung")
submenu_3.add_command(label="Apple")
submenu_3.add_command(label="Motorola")
phone.add_cascade(label="Marca", menu=submenu_3)
submenu_4 = Menu(menu)
submenu_4.add_command(label="Smartwatch")
submenu_4.add_command(label="Fundas")
submenu_4.add_command(label="Vidrio templado")
phone.add_cascade(label="Accesorios", menu=submenu_4)
menu.add_cascade(label="Celulares", menu=phone)

info = Menu(menu, tearoff=0)
info.add_command(label=)
menu.add_cascade(label="Informacion", menu=info)


windows.config(menu=menu)
mainloop()