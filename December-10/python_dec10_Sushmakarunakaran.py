#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy 
n= int (input("enter number of rows and columns"))
a=[]
for i in range(n):
        for j in range(n):
                b=int (input("enter the element"))
                a.append(b)
                
a=numpy.array(a).reshape(n,n)
print(a)
d= numpy.linalg.det(a)
print(d)
                


# In[ ]:




