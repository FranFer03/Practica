sentence = input("Ingrese una frase : ").lower()

space = " "
comma = ","
dot = "."

numbers_space = 0
numbers_dot = 0
numbers_comma = 0

for letter in sentence:
    if letter in space:
        numbers_space += 1
    elif letter in dot:
        numbers_dot += 1
    elif letter in comma:
        numbers_comma += 1

print("Space {} , Comma {} , Dot {}".format(numbers_space, numbers_comma, numbers_dot))