#!/usr/bin/env python
# coding: utf-8

# # RK4
# J.J
# ---
# 
# \begin{equation}
# y_{k+1} = y_{k} + \frac{h}{6} \{ F_{1} + 2 F_{2} + 2 F_{3} + F_{4} \},
# \end{equation}
# con
# 
# \begin{align}
# F_{1} &= f(x_{k},y_{k}), & F_{2} &= f(x_{k} + \frac{h}{2}, y_{k} + \frac{h}{2} F_{1}) \\
# F_{3} &= f(x_{k} + \frac{h}{2}, y_{k} + \frac{h}{2} F_{2}), & F_{4} &= f(x_{k} + h, y_{k} + hF_{3})
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


def F2(x,y,h):
    F2 = f(x+(h/2), y+((h/2)*f(x,y)))
    return F2


# In[4]:


def F3(x,y,h):
    F3 = f(x+(h/2), y+((h/2)*F2(x,y,h)))
    return F3


# In[5]:


def F4(x,y,h):
    F4 = f(x+h,y+(h*F3(x,y,h)))
    return F4


# In[6]:


def RK4(f, X0, final, h): #(ec. dif, condiciones iniciales, punto final de integracion, tamaño de pasos)
    x0, y0 = X0[0], X0[1]
    size =  final/h #tamaño del grid de integracion
    
    X = np.linspace(x0, final, num=int(size))
    Y = np.copy(X)
    Y[0] = y0
    
    for i in range(0, int(size)-1):
        Y[i+1] = Y[i] + (h/6)*(f(X[i], Y[i]) + 2*F2(X[i], Y[i], h) + 2*F3(X[i], Y[i], h) + F4(X[i], Y[i], h))
        
    return X, Y


# In[7]:


#ejemplo
X, Y = RK4(f, [1, 1], 10, 0.01)

plt.plot(X,Y)
plt.show()


# In[ ]:




