# import libraries
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

# SOLUTIONS
# The line in this plot has a slope between 1 and 2, suggesting an order between 1 and 2

        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  f = lambda x: (x**6) - x - 1
  x_0 = 1
  x_1 = 2

  Nmax = 100
  tol = 1.e-14
  root_found = 1.1347241

  (p,pstar,info,it,er_it) = secant(f,x_0,x_1,tol, Nmax, root_found)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)

  header = ['Iterations', 'Error']

  print(tabulate(er_it, headers=header))


  er_it_plus1 = er_it[1:]
  er_it_min1 = er_it[0:-1]
  x_kplus1 = [i[1] for i in er_it_plus1]
  x_k = [i[1] for i in er_it_min1]

  plt.xscale('log')
  plt.yscale('log')

  plt.plot(x_k, x_kplus1)
  plt.show()


def secant(f,x_0,x_1,tol,Nmax,root_found):
  """
  Newton iteration.
  
  Inputs:
    f - function
    x_0  - initial guess 1
    x_1 - initial guess 2
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
  p[0] = x_0
  p[1] = x_1
  p1 = x_1
  for it in range(Nmax):
      p2 = x_1 - f(x_1)*(x_1 - x_0)/(f(x_1) - f(x_0))

      er_lst.append([it, np.abs(p2 - root_found)])

      p[it+2] = p2
      if (abs(p2-p1) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it,er_lst]
      p1 = p2
      x_0 = x_1
      x_1 = p2

  pstar = p2
  info = 1
  return [p,pstar,info,it,er_lst]
        
driver()
