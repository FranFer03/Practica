def metodos(tupla):
    print("Operaciones con tupla")
    print("Cantidad de elementos de la tupla : {}".format(len(tupla)))
    ingreso = int(input("ingrese un valor de la tupla : "))
    numero = tupla.count(ingreso)
    print("Numero de ocurrencia : {}".format(numero))
    indice = tupla.index(ingreso)
    print("Indice {} es {} ".format(ingreso, indice))
    tupla_2 = tupla
    print("Copia : {}".format(tupla_2))
    print(tupla_2*3)
    print("Tipo de {} es : {}".format(tupla, type(tupla)))
    print("Cantidad de lementos de la tupla*3 : {}".format(len(tupla_2*3)))



tupla = (3,4,5,7,3)
metodos(tupla)