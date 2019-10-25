def calcTeleg():
    pay_letter = 0
    pay_digits = 0
    pay_special = 0
    pay_signos = 0
    cadena = input("Mensaje : ").lower()
    abc ="abcdefghijklmnopqrstuvxyw"
    numbers = "0123456789"
    special = "áéíóú"
    signos =",;.:=+-*/¡!¿?"
    for cad in cadena:
        if cad in abc:
            pay_letter += 0.45
        if cad in numbers:
            pay_digits += 0.50
        if cad in special:
            pay_special += 0.75
        if cad in signos:
            pay_signos += 0.20
    print("El total a pagar es : {}".format(pay_signos + pay_special + pay_digits + pay_letter))

calcTeleg()