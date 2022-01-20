#!/usr/bin/env python
# coding: utf-8

# # Método de punto fijo
# J.J
# ---
# Dado que se busca resolver $f(x) = 0$, la función $f$ puede ser reescrita como $f(x) = g(x) - x = 0$. El método de punto fijo está dado por las iteraciones:
# 
# \begin{equation}
# x_{k+1} = g(x_{k}).
# \end{equation}
# 
# El método converge a una raíz si los valores de $x_{k}$ en cada iteración cumplen $|g'(x)| \leq 1$.

# Ejemplo: $f(x) = 2x^{3} - 9x^{2} + 7x + 6 = 0$
# \begin{equation}
# x = \frac{1}{7} \{ -2x^{3} + 9x^{2} - 6 \}
# \end{equation}

# In[1]:


import numpy as np
from sympy import *
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt
init_printing(use_unicode=True)


# In[2]:


#calcular la derivada de f
x = symbols('x')
funcion = 2*x**3 - 9*x**2 + 7*x + 6
gfuncion = (-2*x**3 + 9*x**2 - 6)/7 #escribir la función aqui
dgfuncion = diff(gfuncion, x)
print(str(dgfuncion))


# In[3]:


f = lambdify(x, funcion)
g = lambdify(x, gfuncion)
dg = lambdify(x, dgfuncion)


# In[4]:


X = np.linspace(-1, 4, 100)
plt.plot(X,dg(X), label = 'g´(x)')
plt.ylim(-1,1)
plt.legend()
plt.show()


# La desigualdad se cumple aproximadamente entre en los intervalos $[-0.44, 0.46]$ y $[2.5, 3.34]$, aun que en realidad, en el primer intervalo no converge.

# In[5]:


e = 0.0001 #error
maxit = 100 #iteraciones máximas


# In[6]:


def PuntoFijo(x0, func = g, error = e, iterations = maxit):
    it = 0
    while (abs(f(x0)) > e) and (it < maxit):
        it += 1
        xk = g(x0)
        x0 = xk
    return x0


# In[7]:


sol = PuntoFijo(2.6)
print(sol)


# In[8]:


plt.plot(X, f(X), label='f(x)')
plt.plot(sol,f(sol),'ro')
plt.legend()
plt.show()


# In[ ]:




