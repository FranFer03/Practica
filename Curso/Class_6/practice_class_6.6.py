from tkinter import *
def dolar():
    if conversion.get() != "" and not "," in conversion.get():
        cambio_1 = float(59.6*float(conversion.get()))
        cambio_2 = float(65.76 * float(conversion.get()))
        return cam_dolar.set(cambio_1), cam_euro.set(cambio_2)
    else:
        return cam_dolar.set("Valores invalidos"), cam_euro.set("Valores invalidos")


windows = Tk()
windows.geometry("300x170")
windows.config(bg="snow")

conversion = StringVar()
cam_dolar = StringVar()
cam_euro = StringVar()

eti_tittle = Label(windows, text="Conversion de modena", fg="ivory2", bg="RoyalBlue1", width=60, relief=RAISED, font="Verdana 12 bold italic" ).pack()
eti_1 = Label(windows, text="Ingrese cantidad", font="Verdana 8 bold italic").pack()
entry_conversion = Entry(windows, textvariable=conversion, justify=LEFT).pack()
button_conversion = Button(windows, command=dolar, text="Convertir", width=25, font="Verdana 8 bold italic").pack()
eti_2 = Label(windows, text="Dolar", bg="snow", font="Verdana 8 bold italic", width=40, relief=SUNKEN).pack()
eti_3 = Label(windows, textvariable=cam_dolar, bg="snow").pack()
eti_4 = Label(windows, text="Euro", bg="snow", font="Verdana 8 bold italic", width=40, relief=SUNKEN).pack()
eti_5 = Label(windows, textvariable=cam_euro, bg="snow").pack()


mainloop()