import numpy as np
#import matplotlib.pyplot as plt
import scipy

### SOLUTIONS

#Difference in quad routine: 1.9553247909698257e-11
#Differnece in trapezoid: 0.0005957102942724113
#Differnece in Simpsons: 0.008387824024156831


def f(s):
    return 1/(1 + (s**2))

def trapezoid():
    n_min = 646
    part = np.linspace(-5, 5, n_min)
    #print(part)
    h = part[1] - part[0]
    n = len(part)
    sum_total = 0
    #print(n)
    
    for i in range(1, n):
        sum_total += f(part[0] + i*h)
        
    return (h/2)*(f(part[0]) + 2*sum_total + f(part[-1]))

def simpsons():
    n_min = 56
    part = np.linspace(-5, 5, 50)
    #print(part)
    h = part[1] - part[0]
    n = len(part)
    sum_total_1 = 0
    sum_total_2 = 0
    x_j_1 = []
    x_j_2 = []
    
    #for i in range(1, n):
        #x_j.append(f(part[0] + i*h))
        
    for j in range(1, int((n/2) - 1)):
        x_2j = part[0] + 2*j*h
        sum_total_1 += f(x_2j)
        
    for k in range(1, int(n/2)):
        x_2j_1 = part[0] + 2*k*h - h
        sum_total_2 += f(x_2j_1)
        
    return (h/3)*(f(part[0]) + 2*sum_total_1 + 4*sum_total_2 + f(part[-1]))


scipy_int_1 = scipy.integrate.quad(f, -5, 5)
scipy_int_2 = scipy.integrate.quad(f, -5, 5, epsrel=(10**(-4)))
print(f'Result from SCIPYs quad routine with default tolerance: {scipy_int_1}')
print(f'Result from SCIPYs quad routine with set tolerance of 10^-4: {scipy_int_2}')
    
print(f'Result from composite trapezoid rule with minimum n for tolerance: {trapezoid()}')
print(f"Result from composite Simpson's rule with minimum n for tolerance: {simpsons()}")

print(f'Difference in quad routine: {abs(scipy_int_2[0] - scipy_int_1[0])}')
print(f'Differnece in trapezoid: {abs(scipy_int_1[0] - trapezoid())}')
print(f'Differnece in Simpsons: {abs(scipy_int_1[0] - simpsons())}')