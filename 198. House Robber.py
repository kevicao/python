#!/usr/bin/env python
# coding: utf-8

# In[6]:


#dp[i] = max(num[i] + dp[i - 2], dp[i - 1])

def rob(L):
    dp = [0]*len(L)
    dp[0] = L[0]
    dp[1] = max(L[0], L[1])
    
    for i in range(2, len(L)):
        dp[i]  = max(dp[i-1], dp[i-2] + L[i])
        
    return dp[-1]

print(rob([2,7,9,3,1]))


# In[ ]:




