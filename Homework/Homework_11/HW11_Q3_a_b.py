import numpy as np
import scipy
import math

### Solutions
# See Gradescope submission for answers to questions

x_gamma = 6

def gamma_int(t, x=x_gamma):
    return (t**(x - 1)*(math.e**(-t)))

end_test = 36
n = 1000

def comp_trap(f, n, end):
    parts = np.linspace(0, end, n)
    #print(part)
    h = (parts[-1] - parts[0])/n
    sum_total = 0
    
    for i in range(1, n):
        sum_total += f(parts[0] + i*h)
        
    eval_t = (h/2)*(f(parts[0]) + 2*sum_total + f(parts[-1])) 
    return (eval_t, abs(scipy.special.gamma(x_gamma) - eval_t))




print(f'Gamma function true value for x = {x_gamma}: {scipy.special.gamma(x_gamma)}')
print(f'Composite trapezoid approximation truncated at {end_test} for x = {x_gamma} (value, error): {comp_trap(gamma_int, n, end_test)}')
print(f'Adaptive quadrature routine on 0 to {end_test} for x = {x_gamma} (value, error): {scipy.integrate.quadrature(gamma_int, 0, end_test)}')

