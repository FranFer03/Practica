number_usuary = []
number_of_usuary = ""

while len(number_usuary) < 6:
    while not number_of_usuary.isdigit():
        number_of_usuary = input("Dime un numero : ")
    number_usuary.append(int(number_of_usuary))
    number_of_usuary = ""
    print("Numero añadido!!")

lower = number_usuary[0]

for number in number_usuary:
    if number < lower:
        lower = number

print("El menor numero es ",lower)