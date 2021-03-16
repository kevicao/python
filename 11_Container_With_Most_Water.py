#!/usr/bin/env python
# coding: utf-8

# In[3]: find the two lines that form container with x axis and contain most water. position is i, ai, ai is non negtive integer


# start from outest, and move lower one
#Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction


def res(L):
    n = len(L)
    l = 0
    r = n-1
    
    maxA = min(L[l], L[r])*(r-l)
    while l < r:
        if L[l] < L[r]:
            l += 1
        else:
            r -= 1
        A = min(L[l], L[r])*(r-l)
        if A > maxA:
            maxA = A
            
    return maxA


# In[4]:


res([1,8,6,2,5,4,8,3,7]) #49


# In[ ]:




