#!/usr/bin/env python
# coding: utf-8

# sol:
# reverse the string and convert the problem to find long common substring problem  
# the common substring needs to be at same index in both strings. otherwise it failes when there exists a reversed copy of a non-palindromic substring in some other part of

# # dynamic programing : expand in both ends
# table[i+1][j-1] == 1 && s.charAt(i) == s.charAt(j)
# =>
# table[i][j] == 1
# 
# time n^2 space n^2

# In[3]:


def lps(s):
    n = len(s)
    import numpy as np
    
    matrix = np.zeros((n, n))
    for i in range(n):
        matrix[i][i] = 1
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if j == i+1:
                if s[i] == s[j]:
                    matrix[i][j] = 1
            else:
                if matrix[i+1][j-1] == 1 and s[i] == s[j]:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
                    
    max_L = 1
    for i in range(n):
        for j in range(i,n):
            if matrix[i][j] == 1:
                if j-i+1 > max_L:
                    max_L = j-i+1
    print(matrix)                
    return max_L

lps('cbbd')


# In[ ]:


1 1 1 1 1 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1


# In[24]:


# Expand Around Center; time is n^2 and space 1
# need check two cases: i is the center; center is between i and i+1
def lps(s):
    n = len(s)
    maxL = 1
    for i in range(n-1):
        len1 = expand(s,i,i)
        len2 = expand(s,i,i+1)
        if len1 > maxL:
            maxL = len1
        
        if len2 > maxL:
            maxL = len2
            
    return maxL

def expand(s,l,r):
    while l >= 0 and r <= (len(s) - 1) and s[l] == s[r]:
        l -= 1
        r += 1
        
    return r - l - 1

lps('abbaf')
        


# In[ ]: manachers

https://medium.com/hackernoon/manachers-algorithm-explained-longest-palindromic-substring-22cb27a5e96f


