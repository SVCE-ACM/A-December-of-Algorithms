#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hash(s):
    l=[]
    for i in s:
        l.append(ord(i))
    b=sum(l)
    print(b/len(s))
s=input("Enter the string:")
hash(s)

