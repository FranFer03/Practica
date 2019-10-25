import matplotlib.pyplot as plt
import numpy as np

valores = np.arange(0,2*np.pi, 0.01)
seno = np.sin(valores)
coseno = np.cos(valores)

fig,(gr1, gr2) =plt.subplot(1,2)
fig.subplots_adjust (left=0.15 , wspace=0.7)

box1 = dict(facecolor = "aliceblue", pad = 5, alpha = 0.4)
box2 = dict(facecolor = "darkviolet", pad = 5, alpha = 0.4)

gr1.plot (valores, seno)
gr2.plot(valores, coseno)

plt.show()

