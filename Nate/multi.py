number = int(input("Ingrese numero de tabla : "))

for multiplo in range(1, 11):
    if (number * multiplo) % 2 == 0:
        print("{} x {} ={}".format(number, multiplo, multiplo * number))
