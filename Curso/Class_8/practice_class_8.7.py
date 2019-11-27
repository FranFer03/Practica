from tkinter import *

info = [["Rhiana", "Stay"], ["Arjona", "Iluso"], ["Beyoncé", "Halo"], ["Adele", "Hello"], ["Melendi", "Lapromesa"]]

windows = Tk()

lb_single = Listbox(windows, height=6)
lb_singer = Listbox(windows, height=6)

for singer in info:
    lb_singer.insert(END, singer[0])

for single in info:
    lb_single.insert(END, single[1])


lb_singer.grid(row=2, column=0)
lb_single.grid(row=2, column=1)




mainloop()
