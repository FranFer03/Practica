pokemon_choose = input("Elije tu oponente : Squitle / Charmander / Bulbasaour  : ")

pikachu_life = 100
enemy_life = 0
enemy_damage = 0

if pokemon_choose == "Squitle":
    enemy_life = 90
    enemy_damage = 8
elif pokemon_choose == "Charmander":
    enemy_life = 80
    enemy_damage = 10
elif pokemon_choose == "Bulbasaur":
    enemy_life = 100
    enemy_damage = 5

print("Elegiste de oponente a {}".format(pokemon_choose))

while enemy_life >= 0 and pikachu_life >= 0:
    attack_choose_pikachu = input("Cual ataque vas a elegir? Impactrueno / Bola Voltio :  ")

    if attack_choose_pikachu == "Impactrueno"
        enemy_life -= 10
    elif attack_choose_pikachu == "Bola Voltio"
        enemy_life -= 12

    print("La vida de {} es de {}".format(pokemon_choose, enemy_life))
    print("{} ha lanzado un ataque de {}".format(pokemon_choose, enemy_damage))
    pikachu_life -= enemy_damage

    print("La vida de Pikachu es de {}".format(pikachu_life))

print("El cambate a finalizado")

if enemy_life <= 0
    print("Ganaste")
if pikachu_life <= 0
    print("Perdiste")

