#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#inplace solution
#reverse each word first
#reverse whole string 


# In[9]:


#541

def reverse_k(L, k):
    i = 0
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        while i < len(L):           
            j = min(i+k-1, len(L))
            L = reverse(L, i, j)
            i = i+2*k
    return L
            
def reverse(L, i, j):
    while i < j:
        tmp = L[i]
        L[i] = L[j]
        L[j] = tmp
        i += 1
        j -= 1
        
    return L
L = ["a","b","c","d","e","f","g"]
k = 2  #"bacdfeg"
print(reverse_k(L,2))


# In[ ]:




