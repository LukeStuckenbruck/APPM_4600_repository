# import libraries
import numpy as np
from tabulate import tabulate

# SOLUTIONS
# Root found: 1.1347
# Table copypaste:
# Iterations        Error
#------------  -----------
#           0  0.545904
#           1  0.296015
#           2  0.120247
#           3  0.0268143
#           4  0.00162917
#           5  6.42834e-06
#           6  3.85002e-08
#           7  3.84015e-08
#           8  3.84015e-08
# The error does get smaller with each iteration

        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  f = lambda x: (x**6) - x - 1
  fp = lambda x: 6*(x**5) - 1
  p0 = 2

  Nmax = 100
  tol = 1.e-14
  root_found = 1.1347241

  (p,pstar,info,it,er_it) = newton(f,fp,p0,tol, Nmax, root_found)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)

  header = ['Iterations', 'Error']

  print(tabulate(er_it, headers=header))


def newton(f,fp,p0,tol,Nmax,root_found):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
    root_found - root found from previous iterations used for calculating error
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
    er_lst - list of 1x2 lists containing the iteration number and error
     
  """

  er_lst = []
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)

      er_lst.append([it, np.abs(p1 - root_found)])

      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it,er_lst]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it,er_lst]
        
driver()
