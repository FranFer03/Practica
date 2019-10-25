input_numero = int(input("¿Que numero quieres introducir en la tabla? "))
numeros = []
for numero in range(1, 11):
    numeros.append(numero)

revnumeros = reversed(numeros)

for num in revnumeros:
    print("{} x {} = {}".format(input_numero, num, input_numero * num))