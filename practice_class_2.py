"""leg_1 = float(input("Ingrese el cateto : "))
leg_2 = float(input("Ingrese el 2do cateto : "))
hypotenuse = float(input("Ingrese la hipotenusa : "))"""

number_1 = float(input("Ingrese el 1er lado : "))
number_2 = float(input("Ingrese el 2do lado : "))
number_3 = float(input("Ingrese el 3er lado : "))

if number_1 > 0 and number_2 > 0 and number_3 > 0:
    if number_1 > number_2 and number_1 > number_3:
        hypotenuse = number_1
        calculus = number_3**2 + number_2**2
    elif number_2 > number_1 and number_2 > number_3:
        hypotenuse = number_2
        calculus = number_3 ** 2 + number_1 ** 2
    else:
        hypotenuse = number_3
        calculus = number_2 ** 2 + number_1 ** 2

    if hypotenuse**2 == calculus:
        print("Es un triangulo rectangulo")
    else:
        print("No es un triangulo rectangulo")
else:
    print("Los datos no son validos")