#!/usr/bin/env python
# coding: utf-8

# # Aproximación de integrales
# J.J
# ---
# Ejemplo:  $I = \int_{0}^{\pi/2} \cos(x)dx =1$.

# In[1]:


import numpy as np


# In[2]:


#escribir aqui la funcion y los limites de integracion
def f(x):
    return np.cos(x)

a = 0.
b = (np.pi)/2


# ## Regla del trapecio
# 
# \begin{equation}
# \int_{a}^{b} f(x)dx \approx \left( \frac{b-a}{2} \right) \left[ f(a) + f(b) \right].
# \end{equation}

# In[3]:


def Trapecio(a=a, b=b, f=f):
    return ((b-a)/2)*(f(a)+f(b))


# In[4]:


print(Trapecio())


# ## Regla de Simpson
# 
# \begin{equation}
# \int_{a}^{b} f(x)dx \approx \left( \frac{b-a}{6} \right) \left[ f(a) + 4f \left( \frac{a+b}{2} \right)  + f(b) \right].
# \end{equation}

# In[5]:


def Simpson(a=a, b=b, f=f):
    return ((b-a)/6)*(f(a)+4*f((a+b)/2)+f(b))


# In[6]:


print(Simpson())


# In[ ]:




