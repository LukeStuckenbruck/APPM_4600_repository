import numpy as np
import scipy
import math

### Solutions
# This code approximates gamma with using gaussian quadrature

x_gamma = 8

def gamma_int_gauss(t, x=x_gamma):
    return t**(x - 1) #*(math.e**(-t))

(t, w) = np.polynomial.laguerre.laggauss(5)

f = []
for i in t:
    f.append(gamma_int_gauss(i))

print(f'Gaussian quadrature for x = {x_gamma}: {np.sum(f*w)}')


