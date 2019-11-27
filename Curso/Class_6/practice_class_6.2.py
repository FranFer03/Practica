from tkinter import *
windows = Tk()
def close():
    windows.quit()
def destroy():
    windows.destroy()

btnquit = Button(windows,text="Salir",command=close,width=10).pack(side=LEFT)
btndestroy = Button(windows,text="Destruir",command=destroy,width=10).pack(side=RIGHT)
mainloop()
