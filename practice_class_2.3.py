number_1 = int(input("Ingrese el 1° numeros : "))
number_2 = int(input("Ingrese el 2° numeros : "))
number_3 = int(input("Ingrese el 3° numeros : "))

if number_1 > number_2 and number_1 > 0 and number_2 > number_3:
    print("Ingresado de forma ascendente ")

elif number_1 < number_2 and number_1 < 0 and number_2 < number_3:
    print("Ingresado de forma descendente")

else:
    print("Ingresado de forma aleatoria")