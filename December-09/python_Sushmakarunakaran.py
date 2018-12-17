#!/usr/bin/env python
# coding: utf-8

# In[6]:


import validators
a=input ("enter the string")
validators.url(a)


# In[ ]:


import validators
validators.url("http://google.com")
True
validators.url("http://google")
ValidationFailure(func=url, args={'value': 'http://google', 'require_tld': True})
if not validators.url("http://google"):
    print "not valid"

not valid

