import folium

def marcadores():
    mapa = folium.Map(location=[-27.-65], zoom_start=10)
    folium.Marker(location=[-26.8, -65.2], popup="San Miguel de tucuman", icon=folium.Icon(color="red")).add_to(mapa)
    folium.Marker(location=[-26.9257, -65.3379], popup="Lules", icon=folium.Icon(color="gold")).add_to(mapa)
    folium.Marker(location=[-27.04, -65.42], popup="Famailla", icon=folium.Icon(color="blue")).add_to(mapa)
    folium.Marker(location=[-27.15, -65.52], popup="Monteros", icon=folium.Icon(color="green")).add_to(mapa)
    folium.Marker(location=[-27.34, -65.63], popup="Concepcion", icon=folium.Icon(color="maroon")).add_to(mapa)
    return mapa

def localizaciones():
    lista = ["San Miguel de tucuman", "Lules", "Famailla", "Monteros", "Concepcion"]
    return lista