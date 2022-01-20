#!/usr/bin/env python
# coding: utf-8

# # Método de bisección
# J.J
# ---
# Dada una función continua $f$ en un intervalo cerrado $[a,b]$, si $f(a)f(b) < 0$ se puede asegurar que existe un valor $f(p) = 0$ para algún $p \in [a,b]$.
# 
# El método consiste en escoger un valor $x_{1}$ en el centro del intervalo: $x_{1} = \frac{1}{2}(a+b)$. Si $f(a)f(x_{1}) < 0$ la raíz se encuentra ahora en el intervalo $[a,x_{1}]$ y se procede con otra iteración ahora en el punto $x_{2} =  \frac{1}{2}(a+x_{1})$. En el caso de que el signo opuesto haya sido con $f(b)$, $f(x_{1})f(b) < 0$, la raíz se encuentra en el intervalo $[x_{1},b]$ y la siguiente iteración es entonces $x_{2} = \frac{1}{2}(x_{1}+b)$.
# 
# Siguiendo estos pasos, el método eventualmente disminuye la longitud del intervalo convergiendo a la raíz de la función.

# Ejemplo: $f(x) = 2x^{3} - 9x^{2} + 7x + 6$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def f(x):
    f = 2*x**3 - 9*x**2 + 7*x + 6
    return f


# In[3]:


X = np.linspace(-1, 4, 100)
plt.plot(X,f(X), label = 'f(x)')
plt.legend()
plt.show()


# Hay raices en los intervalos $[-1,0]$, $[1.5, 2.5]$ y $[2.5, 3.5$].

# In[4]:


e = 0.0001 #error


# In[5]:


def Biseccion(a, b, func = f):
    x = (1/2)*(a+b)
    while f(x) > e:
        if f(a)*f(x) < 0:
            Biseccion(a,x)
        elif f(x)*f(b) < 0:
            Biseccion(x,b)
    return x


# In[6]:


sol1 = Biseccion(-1,0)
sol2 = Biseccion(1.5,2.5)
sol3 = Biseccion(2.5,3.5)
print(sol1, sol2, sol3)


# In[7]:


X = np.linspace(-1, 4, 100)
plt.plot(X,f(X), label = 'f(x)')
plt.plot(sol1, f(sol1), 'ro')
plt.plot(sol2, f(sol2), 'ro')
plt.plot(sol3, f(sol3), 'ro')
plt.legend()
plt.show()

