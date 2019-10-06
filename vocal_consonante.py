sentence = input("Ingrese una frase : ").lower()

vowel = ["a", "e", "i", "o","u"]

numbers_vowel = 0
numbers_consonants = 0
for letter in sentence:
    if letter in vowel:
        numbers_vowel += 1
    else:
        numbers_consonants +=1

print("Las vocales son {} y {} consonates".format(numbers_vowel, numbers_consonants))