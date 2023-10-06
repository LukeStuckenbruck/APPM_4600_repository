Nmax = 200

def f(x, y, z):
    return (x**2) + 4*(y**2) + 4*(z**2) - 16

def f_x(x):
    return 2*x

def f_y(y):
    return 8*y

def f_z(z):
    return 8*z

tol = 1e-5

def ellipse(x_0, y_0, z_0, f, Nmax):

    for i in range(1, Nmax):
        x_n1 = x_0 - (f(x_0, y_0, z_0)*f_x(x_0))/((f_x(x_0)**2) + (f_y(y_0)**2) + (f_z(z_0)**2))
        y_n1 = y_0 - (f(x_0, y_0, z_0)*f_y(y_0))/((f_x(x_0)**2) + (f_y(y_0)**2) + (f_z(z_0)**2))
        z_n1 = z_0 - (f(x_0, y_0, z_0)*f_z(z_0))/((f_x(x_0)**2) + (f_y(y_0)**2) + (f_z(z_0)**2))
        
        x_0 = x_n1
        y_0 = y_n1
        z_0 = z_n1

	#x_array.append(x_n1)
        
        if f(x_n1, y_n1, z_n1) < tol:
            return [x_n1, y_n1, z_n1]
        
    return 'error'

print(ellipse(1, 1, 1, f, Nmax))