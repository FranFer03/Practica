cont = 0
aux = ""
number = []

while aux != "0":
    aux = ""
    while not aux.isdigit():
        aux = input("Dime un numero : ")
    number.append(int(aux))
    print("Numero ingresado !!")

for i in number:
    if i != 0:
        cont += 1

print("Largo de la lista : ", cont)
