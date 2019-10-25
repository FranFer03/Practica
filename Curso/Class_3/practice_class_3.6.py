import matplotlib.pyplot as plt
import numpy as np

valores = np.arange(0, 2, 0.01)

seno = np.sin(np.pi * valores)
coseno = np.cos (np.pi *valores)

plt.plot(valores, seno, label="Funcion seno")
plt.plot(valores, coseno, label="Funcion cosseno")
plt.title("Funciones trigonometricas")
plt.legend()
plt.grid()
plt.show()