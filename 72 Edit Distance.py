#!/usr/bin/env python
# coding: utf-8

# In[16]:Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:

Insert a character

Delete a character

Replace a character




def ed(s1, s2):
    mem = [[1000]*(len(s2)+1) for x in range(len(s1)+1)]
    mem[-1] = [x for x in range(len(s2)+1)]
    for i in range(len(s1)+1):
        mem[len(s1)-i][0] = i
    
    for i in range(len(s1)-1, -1, -1):
        for j in range(1, len(s2)+1):
            if s1[len(s1) -1 - i] == s2[j-1]:
                tmp = mem[i+1][j-1]
            else:
                tmp = mem[i+1][j-1] + 1
                
            mem[i][j] = min(mem[i+1][j]+1, mem[i][j-1]+1, tmp)
    
    for x in mem:
        print(x)
    return mem[0][-1]
    
ed('intention', 'execution')


# In[ ]:




