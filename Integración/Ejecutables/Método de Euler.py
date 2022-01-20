#!/usr/bin/env python
# coding: utf-8

# # Método de Euler
# ## Josué Juárez Morales
# -----
# Es un método basado en diferencias finitas para resolver la ecuación diferencial ordinaria
# \begin{align}
# \frac{d}{dx} y(x) = f(x,y), & \ \ \ x \geq a \\
# y(a) = g
# \end{align}
# 
# El dominio de integración es sobre la malla uniforme con tamaño $h$: $x_k = a + kh$, $k = 0, 1, 2, \dotsc$
# 
# En el punto $x_k$, el valor de la solución numérica es $y_k$.
# 
# # Esquema de Euler
# Realizando la serie de Taylor
# \begin{align}
# y(x_{k+1}) &= y(x_{k}) + h \frac{\partial y}{\partial x}(x_{k}) + \frac{h^2}{2} \frac{\partial^2 y}{\partial^2 x}(\xi_{k}) + \cdots \\
#  &= y(x_{k}) + h f(x_{k}, y(x_{k})) + \frac{h^2}{2} \frac{\partial^2 y}{\partial^2 x}(\xi_{k}) + \cdots
# \end{align}
# donde $\xi_{k}$ es un punto desconocido en el intervalo $(x_{k}, x_{k+1})$.
# 
# Al considerar que la segunda derivada de $y$ está acotada y un $h$ pequeño, se puede ignormar el último término de las fórmulas anteriores. La fórmula aproximada de $y$ queda como
# 
# \begin{equation}
# y(x_{k+1}) = y(x_{k}) + h f(x_{k}, y(x_{k}))
# \end{equation}
# 
# # Ejemplo
# 
# Solucionar:
# \begin{align}
# y'(x) &= 3\log{x} + y, & y(1) &= 1
# \end{align}

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#funcion
def f(x, y):
    f = 3*np.log(x) + y
    return f


# In[3]:


def sol_Euler(f, X0, final, h): #(ec. dif, condiciones iniciales, punto final de integracion, tamaño de pasos)
    x0, y0 = X0[0], X0[1]
    size =  final/h #tamaño del grid de integracion
    
    X = np.linspace(x0, final, num=int(size))
    Y = np.copy(X)
    Y[0] = y0
    
    for i in range(0, int(size)-1):
        Y[i+1] = Y[i] + h*f(X[i], Y[i])
        
    return X, Y


# In[4]:


#ejemplo
X, Y = sol_Euler(f, [1, 1], 10, 0.01)

plt.plot(X,Y)
plt.show()

