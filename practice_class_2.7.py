age = int(input("Cual es su edad ?.  "))
price = 100

if 0 < age < 100:
    if age <= 10:
        price *= 0.75
        print("Debe pagar su entrada a = ", price)
    else:
        print("Debe pagar su entrada a = ", price)
else:
    print("Usted no tiene la edad para subir a esta atraccion")