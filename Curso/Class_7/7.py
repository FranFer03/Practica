from tkinter import *

windows = Tk()
windows.geometry("300x200")
valor = 0
fontLbl = "Verdana 14 bold italic"
fontBtn = "Arial 10"

lbl = Label(windows, text="Grid con solumnspan", font=fontLbl).grid(row=0, column=0, columnspan=5)

for fil in range(1, 6):
    for col in range(0, 5):
        cell = Button(windows, text=str(valor), width=5).grid(row=fil, column=col)
        valor += 1


mainloop()