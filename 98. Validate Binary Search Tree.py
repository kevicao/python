#!/usr/bin/env python
# coding: utf-8

# In[14]:


# L = [5,1,4,null,null,3,6] false
#https://leetcode.com/problems/validate-binary-search-tree/solution/
#recursively check left and right
def vbst(L, root = 0, lower = float('-inf'), upper = float('inf')):
    if L[root] < lower or L[root] > upper:
        return False

    if root*2+1 < len(L) and L[root*2+1] != None:
        if not vbst(L, root*2+1, lower, L[root]):
            return False 

    if root*2+2 < len(L) and L[root*2+2] != None:
        if not vbst(L, root*2+2, L[root], upper):
            return False

    return True
   
L = [5,1,4,None,None,3,6]  #False
print(vbst(L))
L = [2,1,3] #true
print(vbst(L))
L = [2,3,3] #Fasle
print(vbst(L))
L = [5,1,6,None,None,4,7] #False
print(vbst(L))


# In[25]:


1 != 1


# In[ ]:




