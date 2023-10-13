

import math
import numpy as np

### "LAZY NEWTON" SOLUTIONS
# "Lazy Newton" does not converge for x_0 = y_0 = 1. x goes off to infinity
# For the initial conditions x_0 = 1, y_0 = -1, "Lazy Newton" converges in 17 iterations. This is still not as fast as Newton's method.
# "Lazy Newton" does not work for the initial conditions x_0 = y_0 = 0 because the Jacobian matrix is singular
# Overall, "Lazy Newton" is not as effective as Newton's method. There are more conditions for which "Lazy Newton" does not work and when
#   it does work it takes more iterations. However, it has the advantage of not needed to compute the Jacobian every time.

def f(x,y):
    return (x**2) + (y**2) - 4

def g(x,y):
    return math.exp(x) + y - 1

def f_dx(x):
    return 2*x

def f_dy(y):
    return 2*y

def g_dx(x):
    return math.exp(x)

def g_dy(y):
    return 1

x1 = 1
y1 = 1

x2 = 1
y2 = -1

x3 = 0
y3 = 0

Jac1 = [[f_dx(x1), f_dy(y1)], [g_dx(x1), g_dy(y1)]]
inv_Jac1 = np.linalg.inv(Jac1)

Jac2 = [[f_dx(x2), f_dy(y2)], [g_dx(x2), g_dy(y2)]]
inv_Jac2 = np.linalg.inv(Jac2)

Jac3 = [[f_dx(x3), f_dy(y3)], [g_dx(x3), g_dy(y3)]]
#inv_Jac3 = np.linalg.inv(Jac3)
# The jacobian for x = y = 0 is a singular matrix and therefore has no inverse
# "Lazy Newton" does not work in this scenario


N_max = 100
tol = 1e-5

def lz_newtons(f, g, inv_Jac, x1, y1):
    iterations = 0
    for i in range(N_max):
        iterations += 1
        f_xy = [f(x1, y1), g(x1, y1)]
        (x_n, y_n) = (x1, y1) - np.dot(inv_Jac,f_xy)
        if abs(x_n - x1) < tol:
            return (f'x = {x_n}, y = {y_n}, Iterations = {iterations}')
        x1 = x_n
        y1 = y_n
    
    return 'error'

#lz_newtons(f, g, inv_Jac2, x1, y1)
# "Lazy Newton" does not converge for x_0 = y_0 = 1. x goes off to infinity

print(lz_newtons(f, g, inv_Jac2, x1, y1))
# For the initial conditions x_0 = 1, y_0 = -1, "Lazy Newton" converges in 17 iterations. This is still not as fast as Newton's method.

#lz_newtons(f, g, inv_Jac3, x1, y1)
# "Lazy Newton" does not work for the initial conditions x_0 = y_0 = 0 because the Jacobian matrix is singular






