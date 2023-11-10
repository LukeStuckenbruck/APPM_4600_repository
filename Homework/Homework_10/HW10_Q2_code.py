import numpy as np
#import matplotlib.pyplot as plt

### SOLUTIONS
# Composite trapezoid rule approximated the integral as 2.754548
# Composite Simpson's rule approximated the integral as 2.738414

def f(s):
    return 1/(1 + (s**2))

def trapezoid():
    part = np.linspace(-5, 5, 50)
    #print(part)
    h = part[1] - part[0]
    n = len(part)
    sum_total = 0
    #print(n)
    
    for i in range(1, n):
        sum_total += f(part[0] + i*h)
        
    return (h/2)*(f(part[0]) + 2*sum_total + f(part[-1]))

def simpsons():
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
    
print(f'Result from composite trapezoid rule: {trapezoid()}')
print(f"Result from composite Simpson's rule: {simpsons()}")