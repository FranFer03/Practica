pay = float(input("Cuanto dinero gasto ? .  "))

if pay > 0:
    if pay < 1000:
        print("Pagar con dinero en efectivo")
    elif 1000 <= pay < 3000:
        print("Pagar con tarjeta de debito")
    elif pay >= 3000:
        print("Pagar con tarjeta de credito")
else:
    print("No mienta!!!. No gano dinero")