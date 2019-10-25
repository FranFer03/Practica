cont = 0
aux = ""
number = []
plus = 0

while aux != "0":
    aux = ""
    while not aux.isdigit():
        aux = input("Dime un numero : ")
    number.append(int(aux))
    print("Numero ingresado !!")

for i in number:
    plus += i
    if i != 0:
        cont += 1

print("Largo de la lista : ", plus/cont)
