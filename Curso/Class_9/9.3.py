import folium
from operator import itemgetter

medallas = [["Atletismo", ["Oro", 886], ["Plata", 981], ["Bronce", 885], ["Finlandia", "9-3-0"], (62.8419, 25.7630)],
            ["Judo", ["Oro", 109], ["Plata", 108], ["Bronce", 218], ["Japon", "2-2-1"], (36.2048, 138.2529)],
            ["Natacion", ["Oro", 490], ["Plata", 486], ["Bronce", 491], ["USA", "23-3-2"], (38.3028, -98.1953)]]

maps = folium.Map()

medallas_oro = sorted(medallas, key=itemgetter(1), reverse=True)
print("Mayor cantidad de medallas de oro: {} ({})".format(medallas_oro[0][0], medallas_oro[0][1][1]))
medallas_plata = sorted(medallas, key=itemgetter(2), reverse=False)
print("Menor cantidad de medallas de plata: {} ({})".format(medallas_plata[0][0], medallas_plata[0][2][1]))
print("Cantidad de medallas en Judo : {}".format(medallas[1][1][1]+medallas[1][2][1]+medallas[1][3][1]))
winner = sorted(medallas, key=itemgetter(4), reverse=True)
print("Ganador de mas medallas {} : {}".format(winner[0][4][0], winner[0][4][1]))

