from tkinter import *

def mostrar():
    if lb.curselection() !=():
        for i in lb.curselection():
            print(lista[i])

windows =Tk()
lista = ["ceibo", "jacaranda", "olivo", "naranjo", "sauce"]
scrollbar = Scrollbar(windows, orient=VERTICAL)
lb = Listbox(windows, height=6 , yscrollcommand=scrollbar.set, selectmode=EXTENDED)
scrollbar.config(command=lb.yview)
scrollbar.pack(side=RIGHT, fill=Y)
lb.pack()

for item in lista:
    lb.insert(END, item)

Button(windows, text="Mostrar", command=mostrar).pack()

mainloop()