import folium

mapa = folium.Map(location=[-27, -65], zoom_start=10)

folium.Marker(location=[-26.8, -65.2], popup='<b><i>San Miguel de Tucuman</i></b><br>-26.8, -65.2', icon=folium.Icon(color="green")).add_to(mapa)
folium.Marker(location=[-26.9257, -65.3379], popup='<b><i>Lules</i></b><br>-26.92, -65.33', icon=folium.Icon(color="red")).add_to(mapa)
mapa.save("mapa1.html")
