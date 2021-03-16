#!/usr/bin/env python
# coding: utf-8

# In[5]:Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.


def mp(L):
    m = len(L)
    n = len(L[0])
    
    dp = [[10000]*n for i in range(m)]
    dp[m-1][n-1] = L[m-1][n-1]
    for i in range(m-2, -1, -1):
        dp[i][n-1] = L[i][n-1] + dp[i+1][n-1]
    for j in range(n-2, -1, -1):
        dp[m-1][j] = L[m-1][j] + dp[m-1][j+1]       
        
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + L[i][j]
            
    return(dp[0][0])

mp([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])


# In[ ]:




