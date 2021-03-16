#!/usr/bin/env python
# coding: utf-8

# In[10]:


# mirror property
#https://www.cnblogs.com/grandyang/p/4315649.html

def gray(n):
    res = [0]
    for i in range(n):
        for j in range(len(res)-1, -1, -1 ):
            res.append(res[j] | 1 << i)
            
    return res
            
gray(2)  


# In[3]:


2 << 1


# In[7]:


for x in range(0):
    print(x)


# In[ ]:





# In[ ]:




