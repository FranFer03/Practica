class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.odometro = 11

    def descripcion(self):
        completed = "Marca: "+self.marca+"\nModel: "+self.modelo+"\nAño : "+str(self.anio)
        return completed.title()
    def leer_odometro(self):
        print("El kilometraje de su auto es ",self.odometro)

    def update_odometro(self, kilometros):
        self.odometro = kilometros

    def sum_kilo(self, kilometros):
        if kilometros >= 0:
            self.odometro += kilometros
        else:
            print("No se puede hacer para atras el kilometraje")

class Auto_electrico(Auto):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.bateria = 70

    def descripcion_bateria(self):
        completed = "Su bateria es de : "+ str(self.bateria)+"KWh."
        print(completed)



my_car = Auto("Ferrari", "California", 2016)
print(my_car.descripcion())
my_car.leer_odometro()
print("\n")
my_tesla = Auto_electrico("Tesla", "Model S", 2016)
print(my_tesla.descripcion())
my_tesla.descripcion_bateria()

