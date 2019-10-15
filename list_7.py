lista_variables = [12, 32, "queso", 34, "Tortilla", 36, "Quesadilla"]
lista_enteros = []
lista_cadena = []


for aux in lista_variables:
    while aux.isdigit():
        lista_enteros.append(int(aux))
        print("Numero ingresado !!")


print(lista_enteros)
#print(lista_cadena)