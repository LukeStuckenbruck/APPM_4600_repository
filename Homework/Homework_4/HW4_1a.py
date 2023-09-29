import math
import numpy as np
from scipy import special
import matplotlib.pyplot as plt

a = 0.138*(10**-6)
t = 60*24*60*60

depth = np.linspace(0, 5, 100)

def T(x,t):
    return 35*special.erf(x/(2*math.sqrt(a*t))) - 15

T_vec = []
for i in depth:
    T_vec.append(T(i,t))

plt.plot(depth, T_vec)
plt.show()