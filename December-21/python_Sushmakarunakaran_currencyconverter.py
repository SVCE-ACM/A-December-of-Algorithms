#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pandas import*
training_set=read_csv('titanic.csv')
training_set.head()
a='male'
male=training_set[training_set.Sex==a]
female=training_set[training_set.Sex=='female']
womens_survival_rate=float(sum(female.Survived))/len(female)
mens_survival_rate=float(sum(male.Survived))/len(male)
print(womens_survival_rate)
print(mens_survival_rate)


# In[ ]:





# In[ ]:




