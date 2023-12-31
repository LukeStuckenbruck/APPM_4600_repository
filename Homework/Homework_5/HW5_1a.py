### SOLUTIONS
#Iteration converges to x = 0.5, y = 0.8661
#With a tolerance of 1e-4
#Uses 14 iterations

import numpy as np

tol = 1e-4

def f(x,y):
    return 3*(x**2) - y**2

def g(x,y):
    return 3*x*(y**2) - (x**3) - 1

x_0 = 1
y_0 = 1

Nmax = 200

def converge(f, g, x_0, y_0, Nmax):
    
    iterations = 0
    
    for i in range(1, Nmax):
        x_n1 = x_0 - (1/6)*f(x_0, y_0) - (1/18)*g(x_0, y_0)
        y_n1 = y_0 - (1/6)*g(x_0, y_0)
        
        x_0 = x_n1
        y_0 = y_n1
        
        iterations += 1
        
        #print(f(x_n1, y_n1))
        #print(g(x_n1, y_n1))
        
        if (np.abs(f(x_n1, y_n1)) < 1e-4) and (np.abs(g(x_n1, y_n1)) < 1e-4):
            return [x_n1, y_n1, iterations]
        
    return [x_n1, y_n1, iterations]

print(converge(f, g, x_0, y_0, Nmax))