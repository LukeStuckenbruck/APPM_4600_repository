import numpy as np
import matplotlib.pyplot as plt

### SOLUTIONS
# Below is the code to plot error for the Pade` approximations and Maclaurin series over the interval [0, 5]

def P_a_c(x):
    return (x - (7/60)*(x**2))/(1 + ((x**2)/20))

def P_b(x):
    return x/(1 + (1/6)*x + (7/360)*(x**4))

def Taylor(x):
    return x - ((x**3)/6) + ((x**5)/120)


x_vec = np.linspace(0, 5, 1000)

error_P_a_c = [abs(P_a_c(i) - np.sin(i)) for i in x_vec]
error_P_b = [abs(P_b(i) - np.sin(i)) for i in x_vec]
error_taylor = [abs(Taylor(i) - np.sin(i)) for i in x_vec]

plt.plot(x_vec, error_P_a_c, label='P_3^3(x) and P_4^2(x)')
plt.plot(x_vec, error_P_b, label='P_3^4')
plt.plot(x_vec, error_taylor, label='Maclaurin Polynomial')

plt.xlabel('x')
plt.ylabel('Error')
plt.title('Error for Pade` Approximations and Maclaurin Series')
plt.legend()

plt.show()
