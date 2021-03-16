#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bt(L):
    min_v = L[0]
    max_p = 0
    
    for i in range(1,len(L)):
        if L[i] < min_v:
            min_v = L[i]
        if L[i] > min_v:
            max_p = max(max_p, L[i] - min_v)
            
    return max_p
        
bt([7,1,5,3,6,4]) #5
bt([7,6,4,3,1]) #0


# In[ ]:




