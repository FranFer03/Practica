from tkinter import *
def suma():
    if number1.get() != "" and number2.get() != "" and not "," in number1.get() and not "," in number2.get():
        resultado = float (float(number1.get())+float(number2.get()))
        return value.set(resultado)
    else:
        return value.set("Valores invalidos")

windows = Tk()
number1 = StringVar()
number2 = StringVar()
value = StringVar()
eti_number1 = Label(windows, text="Ingrese un numero").pack()
ent_number1 = Entry(windows, textvariable=number1, justify="right").pack()
eti_number2 = Label(windows, text="Ingrese un numero").pack()
ent_number2 = Entry(windows, textvariable=number2, justify="right").pack()
bot = Button(windows, text="Sumar", command=suma, width=15).pack()
eti_rest = Label(windows, text="Resultado").pack()
edi_serest = Label(windows, textvariable=value).pack()
mainloop()


