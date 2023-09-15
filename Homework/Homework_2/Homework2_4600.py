#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def f(x):
    y = math.exp(x)
    return (y - 1)


# In[2]:


f(0)


# In[3]:


f(5)


# In[4]:


x = 9.999999995*(10**(-10))
f(x)


# In[6]:


def tay(x):
    return x + (x**2)/(math.factorial(2)) # + (x**3)/(math.factorial(3)) + (x**4)/(math.factorial(4)) + (x**5)/(math.factorial(5))


# In[7]:


testx = 9.999999995*(10**(-10))


# In[8]:


print(tay(testx))


# In[9]:


print(testx)


# In[15]:


import numpy as np

t = np.arange(0, math.pi, (math.pi/30))
print(t)



# In[17]:


y = np.cos(t)
print(y)


# In[26]:


def sum(N):
    sum = 0
    for i in range(0, N):
        #print(t[i])
        #print(y[i])
        sum += t[i]*y[i]
    return sum


# In[33]:


print('The sum is:', sum(30))


# In[38]:


def x(theta, R, delta_r, f, p):
    return R*(1 + delta_r*math.sin(f*theta + p))*math.cos(theta)


# In[39]:


def y(theta, R, delta_r, f, p):
    return R*(1 + delta_r*math.sin(f*theta + p))*math.sin(theta)


# In[47]:


import matplotlib.pyplot as plt

x_vec = []
y_vec = []
theta_vec = np.linspace(0, (2*math.pi), 30)

for i in theta_vec:
    x_vec.append(x(i, 1.2, 0.1, 15, 0))
    y_vec.append(y(i, 1.2, 0.1, 15, 0))

plt.plot(theta_vec, x_vec, label = 'x(theta)')
plt.plot(theta_vec, y_vec, label = 'y(theta)')
plt.ylim(-3,3)
plt.xlabel('theta (R)')
plt.ylabel('x/y(theta)')
plt.legend()


# In[54]:


for i in range(0,10):
    x_vec2 = []
    y_vec2 = []
    p2 = np.random.uniform(0,2)
    for j in theta_vec:
        x_vec2.append(x(j, i, 0.05, 2 + i, p2))
        y_vec2.append(y(j, i, 0.05, 2 + i, p2))
        
    plt.plot(theta_vec, x_vec2)
    plt.plot(theta_vec, y_vec2)
    
plt.xlabel('theta')
plt.ylabel('x/y(theta)')
    


# In[ ]:




