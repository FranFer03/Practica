from tkinter import *
from googletrans import Translator


def traducir_en():
    traduccion = Translator().translate(traducing.get(), src="es", dest="en")
    return face.set(traduccion.text)


def traducir_jp():
    traduccion = Translator().translate(traducing.get(), src="es", dest="ja")
    return face.set(traduccion.text)

windows = Tk()
windows.iconbitmap("C:\Iconos\Translate.ico")
photo_1 = PhotoImage(file="C:\Imagenes\Japon.png")
photo_2 = PhotoImage(file="C:\Imagenes\Inglaterra.png")
windows.geometry("300x150")
imgAncho = 200
imgAlto = 200
windows.config(bd=25)

traducing = StringVar()
face = StringVar()

windows.title("Traductor")

eti_1 = Label(windows, text="Traducir texto", fg="Black").pack()
ingres_1 = Entry(windows, textvariable=traducing, justify="left").pack()
botton_en = Button(windows, text="Ingles", image=photo_2, width=imgAncho, height=imgAlto, command=traducir_en).pack(side=LEFT)
botton_jp = Button(windows, text="Japones", image=photo_1, width=imgAncho, height=imgAlto, command=traducir_jp).pack(side=RIGHT)
eti_2 = Label(windows, text="Traduccion", fg="Black").pack()
eti_traduccion = Label(windows, textvariable=face).pack()


mainloop()