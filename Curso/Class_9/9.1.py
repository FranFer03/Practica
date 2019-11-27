import folium

maps = folium.Map(location=[-27, -65], zoom_start=5)

folium.CircleMarker(location=[48.13, 11.57], radius=80, popup="Munchen", color="red", fill=True,
                    fill_color="red").add_to(maps)
folium.CircleMarker(location=[-26.9257, -65.3379], radius=50, popup="Lules", color="purple", fill=True,
                    fill_color="purple").add_to(maps)

maps.save("mapa2.html")
