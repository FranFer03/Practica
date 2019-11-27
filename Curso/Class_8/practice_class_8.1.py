from tkinter import *
"""
def text1():
    windows = Tk()
    texto = Text(windows, height=2, width=30).pack()
    mainloop()
"""
def text2():
    windows = Tk()
    texto = Text(windows, height=5, width=30)
    texto.pack()
    mensaje = """La historia de la natacion se remonta en laprehistoria,ente los egipcios,cuyospasis tenia mucha tierra"""
    texto.insert(END, mensaje)
    mainloop()

text2()