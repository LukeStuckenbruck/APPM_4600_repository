import numpy as np
import matplotlib.pyplot as plt

### SOLUTIONS
# Plots for N = 5, 10, 20, and 21 are in GitHub
# the polynomial plot passes -100 when N goes from 20 to 21

def f(x):
    return 1/(1 + ((10*x)**2))

N = 10

i = list(range(1, N + 1))
h = 2/(N - 1)
x_i = np.zeros(len(i))

count = 0
for j in i:
    x_i[count] = -1 + (j - 1)*h
    count += 1
    
def V_matrix(x_i, n):
    shape = (n, n)
    v_matrix = np.zeros(shape)
    
    row = 0
    column = 0
    for i in x_i:
        for p in range((n - 1), -1, -1):
            v_matrix[row][column] = i**p
            column += 1
        row += 1
        column = 0
        
    return v_matrix

#print(V_matrix(x_i, N))

inv_V = np.linalg.inv(V_matrix(x_i, N))

y_vec = np.zeros(len(x_i))

count1 = 0
for i in x_i:
    y_vec[count1] = f(i)
    count1 += 1
    
#print(y_vec)

coeffs = np.dot(inv_V, y_vec)
#print(coeffs)

def poly(x, coeffs):
    total = 0
    exp = 0

    for i in reversed(coeffs):
        total += i*(x**exp)
        exp += 1
        
    return total

fine_grid = np.linspace(-1,1,1001)
poly_y = np.zeros(len(fine_grid))

count2 = 0
for i in fine_grid:
    poly_y[count2] = poly(i,coeffs)
    count2 += 1
#print(poly_y)

plt.plot(x_i, y_vec, 'o')
plt.plot(fine_grid, f(fine_grid))
plt.plot(fine_grid, poly_y)

plt.show()
