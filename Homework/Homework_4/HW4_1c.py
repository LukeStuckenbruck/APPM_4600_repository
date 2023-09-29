# import libraries
import numpy as np
from scipy import special
import math

# SOLUTIONS
# with x_0 = 0.01, approximate depth is 0.3385
# with x_0 = x_bar = 2, same result is found but using one more iteration (11 
# instead of 10)

        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  alpha = 0.138*(10**(-6))
  time = 60*24*60*60

  f = lambda x: 35*special.erf(x/(np.sqrt(alpha*time))) - 15
  fp = lambda x: (70*math.exp((-x**2)/(4*alpha*time)))/np.sqrt(np.pi)
  p0 = 2

  Nmax = 100
  tol = 1.e-13

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]
        
driver()
