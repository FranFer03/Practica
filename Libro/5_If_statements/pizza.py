available_toppings = ["anchoas", "picante", "peperoni", "extra cheese", "pinea"]
requested_toppings = ["anchoas", "zorrino", "picante"]

for requested in  requested_toppings:
    if requested  in available_toppings:
        print("Añadiendo "+requested+" para que quede como le gusta a usted")
    else:
        print("No tenemos "+requested+" vaya a llorar en la casa")

print("Su pizza esta finalizada")