#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data=pd.read_excel("EXCHANGE RATES.xlsx")
a=input("enter the form country")
b=input("enter the to country")
c=int(input("enter the amount to be transferred"))
d=data[data.LOCATION==a]
e=data[data.LOCATION==b]
f=float(c / float (d.VALUE))*float (e.VALUE)
print("amount in ")
print(b)
print("is")
print(f)
    


# In[ ]:




