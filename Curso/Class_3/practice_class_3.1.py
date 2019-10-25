import random
def age():
    mayor, menor = 0, 0
    for i in range(0, 50):
        edad = random.randrange(1, 75)
        print("", edad ,end="")
        if edad > 21:
            mayor += 1
        elif edad < 21:
            menor += 1
    print("\nMayores a 21 : ", end="")
    for i in range(mayor):
        print("*", end="")

    print("\nMenor a 21 : ", end="")
    for i in range(menor):
        print("*", end="")

age()