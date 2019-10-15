from numpy import *
buy = array([2*25.90, 3*12, 1*35])
pay = 0

for item in buy:
    pay += item

print("Monto total : ",pay)