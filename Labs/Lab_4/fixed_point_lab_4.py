# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: (10/(x + 4))**(1/2)
# fixed point is alpha1 = 1.4987....

#     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 10
     tol = 1e-6
     #it_vector = np.zeros((Nmax,1))
     #print(it_vector)

# test f1 '''
     x0 = 1.5
     [xstar,ier,it_vector] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('The vector of fixed points is:',it_vector)

     [xstar_ak, ak_vector] = aitkins(x0, Nmax, tol, it_vector)
     print('the approximate fixed point is:',xstar_ak)
     print('The vector of fixed points is:',ak_vector)
    
#test f2 '''
#     x0 = 0.0
#     [xstar,ier,it_vector] = fixedpt(f2,x0,tol,Nmax)
#     print('the approximate fixed point is:',xstar)
#     print('f2(xstar):',f2(xstar))
#     print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):

    it_vector = np.zeros((Nmax,1))

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       it_vector[count] = x0
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier,it_vector]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, it_vector]

# define routines
def aitkins(x0,Nmax,tol,it_vector):

    ak_vector = np.zeros((Nmax,1))

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <(Nmax - 3)):
       ak_vector[count] = x0
       count = count +1

       x1 = it_vector[count] - ((it_vector[count + 1] - it_vector[count])**2)/(it_vector[count + 2] - 2*it_vector[count + 1] + it_vector[count])

       if (abs(x1-x0) <tol):
          xstar_ak = x1
          return [xstar_ak,ak_vector]
       x0 = x1

    if type(x1) == Float and (x1 > 0):
       xstar_ak = x1
    ier = 1
    return [xstar_ak, ak_vector]
    # ECCR 244
    

driver()