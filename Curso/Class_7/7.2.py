from tkinter import *


def golosina():
    return message.set("Informacion de golosinas")


windows = Tk()
windows.geometry("280x320")
windows.title("Market")
font_lbl = "Arial 10 bold"

market = ["Golosina", "Lacteos", "Bebidas", "Limpieza", "Jugeteria", "Bazar"]
bot = []
i = 0
message = StringVar()

lbl_tittle = Label(windows, text="Market", font=font_lbl).grid(row=0, column=0, columnspan=5)
for fil in range(1, 3):
    for col in range(0, 3):
        cell = Button(windows, text=market[i], width=10)
        bot.append(cell)
        cell.grid(row=fil, column=col)
        i += 1
bot[0].config(command= golosina)

end = Label(windows, textvariable=message, width=30).place(x=30, y=150)


mainloop()
