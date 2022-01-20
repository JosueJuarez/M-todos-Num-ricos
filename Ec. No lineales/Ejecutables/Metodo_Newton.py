#!/usr/bin/env python
# coding: utf-8

# # Método de Newton
# J.J
# ---
# \begin{equation}
# x_{k+1} = x_{k} - \frac{f(x_{k})}{f'(x_{k})}
# \end{equation}

# Ejemplo: $f(x) = x^{2} + 3x +1$

# In[1]:


import numpy as np
from sympy import *
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt
init_printing(use_unicode=True)


# In[2]:


#calcular la derivada de f
x = symbols('x')
funcion = 1 + 3*x + x**2 #escribir la función aqui
dfuncion = diff(funcion, x)
print(str(dfuncion))


# In[3]:


f = lambdify(x, funcion)
df = lambdify((x), dfuncion)


# In[4]:


e = 0.0001 #error
maxit = 1000000 #iteraciones máximas
x0 = 2. #punto inicial


# In[5]:


def NewtonR(x0, func = f, dfunc = df, error = e, iterations = maxit):
    it = 0
    while (abs(f(x0)) > e) and (it < maxit):
        it += 1
        x0 = x0 - f(x0)/df(x0)
    return x0


# In[6]:


sol = NewtonR(x0)
print(sol)


# In[7]:


X = np.linspace(-4, 2, 100)
plt.plot(X, f(X))
plt.plot(sol,f(sol),'ro')
plt.show()


# In[ ]:




