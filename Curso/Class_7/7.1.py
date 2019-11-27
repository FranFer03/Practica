from tkinter import *


def control():
    if price.get() != "" and quantity.get() != "" and not "," in price.get() and not "," in quantity.get():
        if float(price.get()) > 0 and float(price.get()) > 0:
            return True
        else:
            return False
    else:
        return False


def calculo():
    if control() == True:
        value = float(float(price.get()) * float(quantity.get()))
        return total.set(value), message.set(
            "Producto : {}\n Cantidad: {}\nPrecio: {}\nTotal: {}".format(item.get(), quantity.get(), price.get(),
                                                                         total.get()))
    else:
        return total.set("Valores erroneos")


def boar():
    windows.focus_set()
    return price.set(""), message.set(""), quantity.set(""), total.set(""), item.set("")


windows = Tk()
windows.geometry("280x320")
windows.title("Market")

price = StringVar()
quantity = StringVar()
item = StringVar()
total = StringVar()
message = StringVar()

lbl_item = Label(windows, text="Producto").place(x=15, y=10)
entry_item = Entry(windows, textvariable=item, bd=5, justify=LEFT).place(x=90, y=10)
lbl_price = Label(windows, text="Precio").place(x=15, y=50)
entry_price = Entry(windows, textvariable=price, bd=5, justify=LEFT).place(x=90, y=50)
lbl_quantity = Label(windows, text="Precio").place(x=15, y=90)
entry_quantity = Entry(windows, textvariable=quantity, bd=5, justify=LEFT).place(x=90, y=90)
bt_total = Button(windows, text="Calcular", command=calculo).place(x=70, y=140)
bt_borrar = Button(windows, text="Borrar", command=boar).place(x=150, y=140)
lbl_total_tittle = Label(windows, text="Total $", bd=5).place(x=15, y=180)
lbl_total = Label(windows, textvariable=total, bd=5, relief=GROOVE, width=20, height=1, bg="snow").place(x=90, y=180)
lbl_message = Label(windows, textvariable=message, relief=GROOVE, width=30, height=6, bd=5, bg="snow").place(x=30,
                                                                                                             y=210)
mainloop()
