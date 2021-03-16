#!/usr/bin/env python
# coding: utf-8

# In[13]:


# find the max height up to the given point from left end and right end, 
# O(n)
def tw(L):
    if len(L) == 0:
        return 0
    left_max = [L[0]]
    for i in range(1,len(L)):
        left_max.append(max(left_max[i-1], L[i]))
    
    right_max = [0]*len(L)
    right_max[-1] = L[-1]
    for i in range(len(L)-2,-1, -1):
        right_max[i] = max(right_max[i+1], L[i])
    
    ans = 0
    for i, x in enumerate(L):
        ans += min(left_max[i], right_max[i]) - L[i]
        
    return ans

tw([0,1,0,2,1,0,1,3,2,1,2,1])


# In[ ]:




