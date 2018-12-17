#!/usr/bin/env python
# coding: utf-8

# In[18]:


import inflect
p = inflect.engine()
a=input("enter first string")
b=input("enter second input")
if b.isdigit():
    if b=="1" or b=="-1" :
        if a[-1]=="s":
            print(p.plural(a))
        else :
            print (a)
    else :
        if a[-1]== "s" :
            print(a)
        else :
            print(p.plural(a))
else :
    if a[1:3]== b[1:3] :
        if a[-1]== "s" :
            e = p.plural(a)
            print ("singular :",e)
            print ("plural :",a)
        else :
            f = p.plural(a)
            print ("singular :",a)
            print ("plural :",f)
    else :
        print ("invalid input")


# In[ ]:




