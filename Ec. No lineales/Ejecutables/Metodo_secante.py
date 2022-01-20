#!/usr/bin/env python
# coding: utf-8

# # Método de la secante
# J.J
# ---
# Está dado por las iteraciones
# \begin{equation}
# x_{i+1} = x_{i} - \frac{f(x_{i})}{d_{i}},
# \end{equation}
# con
# \begin{equation}
# d_{i} = \frac{f(x_{i})-f(x_{i-1})}{x_{i} - x_{i-1}}.
# \end{equation}

# Ejemplo: $f(x) = x^{2} + 3x +1$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def f(x):
    f = x**2 + 3*x + 1
    return f


# In[3]:


X = np.linspace(-3, 1, 100)
plt.plot(X, f(X))


# In[4]:


e = 0.0001 #error
maxit = 1000 #iteraciones máximas


# In[5]:


def Secante(x0, x1, func = f, error = e, iterations = maxit):
    it = 0
    while it < maxit:
        it += 1
        x = x1 - ((x1-x0)/(f(x1)-f(x0)))*f(x1)
        if abs(f(x)) > e:
            x0 = x1
            x1 = x
        else:
            break
    return x


# In[6]:


sol1 = Secante(-3.,-2.)
sol2 = Secante(-1.,0.)
print(sol1)
print(sol2)


# In[7]:


X = np.linspace(-3, 1, 100)
plt.plot(X, f(X))
plt.plot(sol1,f(sol1),'ro')
plt.plot(sol2,f(sol2),'ro')
plt.show()


# In[ ]:




