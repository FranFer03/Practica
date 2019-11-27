class alumno:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def interface(self):
        print("Alumno: ",self.name)
        print("Nota: ",self.points)
    def resultado(self):
        if self.points < 5:
            print("El alumno desaprobo")
        else: print("El alumno aprobo")

pichon = alumno("Eduardo",7)
pichon.interface()
pichon.resultado()