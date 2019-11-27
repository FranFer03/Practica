from tkinter import *

def check2():
    def info():
        print(".......\nTeclado: {}\nMouse: {}".format(var1.get(), var2.get()))
    windows = Tk()
    var1 = IntVar()
    var2 = IntVar()
    check1 = Checkbutton(windows, text="Teclado", variable=var1).grid(row=0, sticky=W)
    check2 = Checkbutton(windows, text="Mouse", variable=var2).grid(row=1, sticky=W)
    Button(windows, text="Info", width=20, command=info).grid(row=2, sticky=W)
    mainloop()

check2()