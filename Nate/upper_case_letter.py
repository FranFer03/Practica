sentence = input("Ingrese una frase : ")

capital_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
numbers_capital_letter = 0

for letter in sentence:
    if letter in capital_letter:
        numbers_capital_letter +=1

print("Mayuscula {} ".format(numbers_capital_letter))