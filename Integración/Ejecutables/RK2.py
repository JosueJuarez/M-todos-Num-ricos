#!/usr/bin/env python
# coding: utf-8

# # RK2
# J.J
# ---
# 
# \begin{equation}
# y'_{k+1} = y_{k} + h f(x_{k},y_{k}),
# \end{equation}
# \begin{equation}
# y_{k+1} = y_{k} + \frac{h}{2} [f(x_{k},y_{k}) + f(x_{k+1},y'_{k+1})],
# \end{equation}
# con $k = 0, 1, 2, ...$
# 
# O Bien
# 
# \begin{equation}
# y_{k+1} = y_{k} + h F(x_{k},y_{k}),
# \end{equation}
# con
# \begin{equation}
# F(x,y) \equiv \frac{1}{2} \{ f(x,y) + f(x+h, y+hf(x,y)) \}
# \end{equation}

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#funcion
def f(x, y):
    f = 3*np.log(x) + y
    return f


# In[3]:


def F(x,y,h):
    F = (1/2)*(f(x,y) + f(x+h, y+h*f(x,y)))
    return F


# In[4]:


def RK2(f, X0, final, h): #(ec. dif, condiciones iniciales, punto final de integracion, tamaño de pasos)
    x0, y0 = X0[0], X0[1]
    size =  final/h #tamaño del grid de integracion
    
    X = np.linspace(x0, final, num=int(size))
    Y = np.copy(X)
    Y[0] = y0
    
    for i in range(0, int(size)-1):
        Y[i+1] = Y[i] + h*F(X[i], Y[i], h)
        
    return X, Y


# In[5]:


#ejemplo
X, Y = RK2(f, [1, 1], 10, 0.01)

plt.plot(X,Y)
plt.show()


# In[ ]:




