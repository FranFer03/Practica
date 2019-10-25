day = input("Ingrese el dia de la semana : ").title()

if day == "Lunes":
    print("Con la profesora Bety")
elif day == "Viernes":
    print("Hoy la Motok")
elif day == "Sabado":
    print("A salir de peda")
elif day == "Domingo":
    print("Sale asaduki")
elif day == "Martes" or day == "Miercoles" or day == "Jueves":
    print("Feriado")
else:
    print("Usted no aprende los dias me parece o no sabe escribir")