

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1 + (x**2))

n = 20
x_int = np.linspace(-5,5,n)

def Lagrange(f, x_int, x):
    L_x = 0
    for i in x_int:
        l_xj = 1
        for j in x_int:
            if j == i:
                continue
            else:
                l_xj *= (x - j)/(i - j)
                
        L_x += f(i)*l_xj
        
    return L_x

y_Lagrange = Lagrange(f, x_int, x_int)

plt.plot(x_int, y_Lagrange)
plt.title(f'Lagrange for n = {n}') 
plt.show()


