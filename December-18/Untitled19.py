#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import time
data=pd.read_excel("PASSWORD.xlsx")
a=input("enter the password")
b=time.time()
c=data[data.password==a]
d=time.time()
print (d)


# In[ ]:




