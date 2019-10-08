from math import *
lat_1 = -26.831288
lat_2 = -65.209725
lon_1 = -26.832292
lon_2 = -65.20512
radio = 6371

def calcu():
    a = radians((lat_2 - lat_1)/2)
    a = sin(a)*sin(a)
    b = radians((lon_2 - lon_1)/2)
    b = sin(b)*sin(b)
    semi = 2*radio*asin(sqrt(a**sin(a) + cos(lat_1)*cos(lat_2)*b))
    return semi

print("Distancia : {} KM \t Equivalente : {} M ".format(calcu(), calcu()*1000))