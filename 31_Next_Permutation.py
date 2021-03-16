#!/usr/bin/env python
# coding: utf-8

# In[20]:Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).



def next_p(L):
    import copy
    i = len(L)-1
    while i > 0 and L[i] < L[i-1]:
        i -= 1
    if i == 0: 
        #reverse
        tmp = copy.deepcopy(L)
        for k in range(len(L)):
            L[k] = tmp[len(L)-k-1]
        
    else:
        j = i
        while L[i-1] < L[j] and j < len(L) -1:
            j += 1

        tmp = L[i-1]
        L[i-1] = L[j]
        L[j] = tmp
        
        #now reverse
        tmp = copy.deepcopy(L)
        count = 0
        for k in range(i, len(L)-1):
            L[k] = tmp[len(L)-1-count]
            count += 1
        
    print(L)
        

next_p([1,2,3]) 
next_p([3,2,1])
next_p([1,1,5])


# In[ ]:




