#!/usr/bin/env python
# coding: utf-8

# # Interpolación de Lagrange
# J.J
# ---
# Dado un conjunto de nodos de interpolación $\{ x_{0}, x_{1}, \ldots, x_{n} \}$ y los valores $\{ f_{0}, f_{1}, \ldots, f_{n} \}$ de una función $f(x)$. La aproximación $f(x) \approx L_{n}(f;x) \forall x \in [x_{0},x_{n}]$ recibe el nombre de interpolación polinomial y
# 
# \begin{align}
# L_{n}(f;x) &= \sum_{i=0}^{n} p_{ni}(x) f_{i}, & p_{ni} = \prod_{j=0,j\neq 1}^{n} \frac{x - x_{j}}{x_{i} - x_{j}}.
# \end{align}

# Ejemplo: Interpolar el perfil de la función $f(x) = ln(x), x \in [0,4]$ con el conjunto de puntos $\{ \, (1.0, 0.0), \, (1.7, 0.5306282510621704), \, (2.6, 0.9555114450274363), \, (3.0, 1.0986122886681098), \, (3.4, 1.2237754316221157), \, (4.0, 1.3862943611198906) \, \}$

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


puntos = [(1.0, 0.0), (1.7, 0.5306282510621704), (2.6, 0.9555114450274363), (3.0, 1.0986122886681098), (3.4, 1.2237754316221157), (4.0, 1.3862943611198906)]
n = len(puntos)


# In[3]:


def p(x, i, n=n, X=puntos):
    p = 1
    for j in range(0, n):
        if j == i:
            continue
        else:
            p *= ((x-X[j][0])/(X[i][0]-X[j][0]))
    return p


# In[4]:


def f(x, n=n,X=puntos): #funcion aproximada
    f = 0
    for i in range(0, n):
        f += p(x,i)*X[i][1]
    return f


# In[8]:


x = np.linspace(1, 4, 100)
plt.scatter(*zip(*puntos))
plt.plot(x, f(x))
plt.show()


# In[ ]:




