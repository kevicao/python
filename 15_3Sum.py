#!/usr/bin/env python
# coding: utf-8

#  find all a + b + c = 0 in an array of integers

# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# In[14]: loop from left to right to see if each can be included in one. The check could be 2sum or narrow down from both end in sorted array


def sum3(L):
    L = sorted(L)
    result = []
    
    for i in range(len(L)-2):
        l = i+1
        r = len(L)-1
        while l < r:
            print(i, l,r)
            if L[l] + L[r] + L[i] > 0:
                r -= 1
            elif L[l] + L[r] + L[i] < 0:
                l += 1
            else:
                result.append([L[i], L[l], L[r]])
                break
                
    return result
    


# In[15]:


sum3([-4, -1, -1, 0, 1, 2])


# In[ ]:




