radio = float(input("Ingrese la radio : "))
height = float(input("ingrese la altura : "))

volumen = float(radio * radio * 3.14 * height)


if (volumen >300):
    print("Su volumen es mayor a 300 ")
else:
    print("El volumen es menor a 300")
