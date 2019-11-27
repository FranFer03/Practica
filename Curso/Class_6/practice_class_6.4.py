from tkinter import *

windows = Tk()
text1 = StringVar()
text2 = StringVar()
windows.iconbitmap("C:\Iconos\Argentina.ico")
photoeti_1 = PhotoImage(file="C:\Imagenes\Pacha.gif")
photoeti_2 = PhotoImage(file="C:\Imagenes\\tenor.gif")
imgAncho = 300
imgAlto = 200

text1.set("Pachamama (Madre Tierra) o Mama Pacha es una diosa totémica de los incas representada por el planeta Tierra\n"+
          " a la que se brindaban presentes en las ceremonias agrícolas y ganaderas en el mundo andino\n"+
          "Es el núcleo del sistema de creencias de actuación ecológico-social entre los pueblos indígenas de los Andes\n"+
          "Centrales de América del Sur")
text2.set("Miles de jujeños y turistas, congregados en los mojones de las comparsas que en todo Jujuy celebran el carnaval,\n"
          "desenterraron al mítico Pujllay, el diablo carnavalero de la alegría que andará suelto durante nueve días.")
windows.title("Pachamama")
windows.config(bg="navajowhite")

eti_title_1 = Label(windows, text="Cultura Argentina", bg="peru", fg="white", font="Verdana 16 bold italic", width=50).pack()
etiphoto_1 = Label(windows, image=photoeti_1, width=imgAncho, height=imgAlto).pack()
eti_text1 = Label(windows, textvariable=text1, bg="navajowhite", fg="black", font=("Helvatica", 12)).pack()
eti_title_2 = Label(windows, text="Carnaval Jujuy", bg="peru", fg="white", font="Verdana 16 bold italic", width=50).pack()
etiphoto_2 = Label(windows, image=photoeti_2, width=imgAncho, height=imgAlto).pack()
eti_text2 = Label(windows, textvariable=text2, bg="navajowhite", fg="black", font=("Helvatica", 12)).pack()




windows.mainloop()
