import folium
from operator import itemgetter

censo2010 = [["Capital", 548866, (-26.8, -65.1946), "marron"],
            ["Leales", 54949, (-27.160636, -65.1198), "Blue"],
            ["Lules", 45049, (-26.9257, -65.3379), "red"]
            ]
maps = folium.Map(location=[-27, -65], zoom_start=5)
censo2010.sort(key=itemgetter(1), reverse=True)

for item in censo2010:
    folium.CircleMarker(location=item[2], radius=20, popup=item[0], color=item[3], fill=True, fill_color=item[3]).add_to(maps)

maps.save("mapa3.html")