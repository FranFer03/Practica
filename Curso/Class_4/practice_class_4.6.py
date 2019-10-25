import tkinter.filedialog as tk
ruta = tk.askopenfilename()
lectura = open(ruta,"r")
print(lectura.read())