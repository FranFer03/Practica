pokemon_choose = input("Elije tu oponente : Squitle / Charmander / Bulbasaour  : ")

pikachu_life = 100
enemy_life = 0

if pokemon_choose == "Squitle":
    enemy_life = 90
    enemy_damage = 8
elif pokemon_choose == "Charmander":
    enemy_life = 80
    enemy_damage = 10
elif pokemon_choose == "Bulbasaur":
    enemy_life = 100
    enemy_damage = 5

print("Elegiste ")

while enemy_life >= 0 and pikachu_life >= 0:
    attack_choose = input("Cual ataque vas a elegir? ")
    print("{} ha lanzado un ataque de {}".format(pokemon_choose, enemy_damage))