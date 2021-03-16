#!/usr/bin/env python
# coding: utf-8

# In[13]:


# https://www.cnblogs.com/grandyang/p/4257740.html

def wb(s, wordDict):
    mem = [0]*(len(s)+1)
    
    mem[0] = 1
        
    for i in range(1, len(s)+1):
        for j in range(i):
#             print(i,j)
            if mem[j] == 1 and s[j:i] in wordDict:
                mem[i] = 1
                break
    
    print(mem)
    return mem[-1]
            
wb("leetcode", ["leet", "code"]) #true
wb("applepenapple",["apple", "pen"]) #true
wb("catsandog", ["cats", "dog", "sand", "and", "cat"]) #false
wb("catsand", ["cats", "dog", "sand", "and", "cat"])


# In[ ]:




