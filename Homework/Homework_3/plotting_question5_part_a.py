import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-2, 8, 1000)

def f(x):
    return x - 4*np.sin(2*x) - 3

#xaxis = np.array([])

#yaxis = np.array([])


plt.plot(x, f(x))
plt.axhline(y = 0, color = 'r', linestyle = '-')
plt.show()