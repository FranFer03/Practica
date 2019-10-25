import matplotlib.pyplot as plt
import numpy as np

arreglo1 = np.array([1, 2, 3])
arreglo2 = np.array([-2, 5, 11])
arreglo3 = np.array([0, 7, 23])

plt.plot(arreglo1, arreglo2, "ro", arreglo2, arreglo3, "bs", arreglo1, arreglo3, "g^")
plt.axis([-5, 25, -5, 25])
plt.title("Graficando arrays", color="r", fontsize=16, bbox={"facecolor": "lemonchiffon"})
plt.grid()
plt.show()