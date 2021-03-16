#!/usr/bin/env python
# coding: utf-8

# In[20]:


#pq store the index of node in next level, so process pq one by one and build next pq (tmp_l)
def level_trav(L):
    pq = [0]
    ress = []
    res = []
    
    tmp_l = []
    
    depth = 0

    while pq:
        depth += 1
        for i in range(len(pq)): 

            tmp = pq[i]
            res.append(L[tmp])

            if tmp*2 + 1 < len(L) and L[tmp*2+1] is not None:
                tmp_l.append(tmp*2 + 1)
            
            if tmp*2 + 2 < len(L) and L[tmp*2+2] is not None:
                tmp_l.append(tmp*2 + 2)
                
        ress.append(res)
        res = []
        pq = tmp_l[:]
        tmp_l = []
            
    return (ress, depth)
    
level_trav([3,9,20,None,None,15,7])


# In[ ]:





# In[ ]:




