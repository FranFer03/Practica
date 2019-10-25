import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
y = x
plt.figure(facecolor="lightyellow")
plt.plot(x, y,label="Lineal")
plt.xlabel("x", color="firebrick")
plt.ylabel("y", color="firebrick")
plt.legend()
plt.grid()
plt.show()