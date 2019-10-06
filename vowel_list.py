sentence = input("Ingrese una frase : ").lower()

vowel = ["a", "e", "i", "o","u"]
vowel_list = []

for letter in sentence:
    if letter in vowel:
        vowel_list.append(letter)


print("Las vocales son = {}".format(vowel_list))