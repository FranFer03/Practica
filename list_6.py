aux = ""
number = []

multi = int(input("Numero por el cual se van a multiplicar : "))

while aux != "0":
    aux = ""
    while not aux.isdigit():
        aux = input("Dime un numero : ")
    if aux != "0":
        number.append(int(aux)*multi)
        print("Numero ingresado !!")

print(number)