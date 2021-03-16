#!/usr/bin/env python
# coding: utf-8

# In[12]: Given the head of a linked list, remove the nth node from the end of the list and return its head.


d = dict()
d['head'] = [1, 1]
d[1] = [2, 2]
d[2] = [3, 3]
d[3] = [4, 4]
d[4] =[5, 'end']

#traverse a list
def pl(d):
    pointer = 'head'
    print(d[pointer][0])
    while d[pointer][1] != 'end':
        pointer = d[pointer][1]
        print(d[pointer][0])
        
    return None
        
pl(d)


# In[13]:


#delete the nth node from the end, in one pass
#record before and after node pointer for each node 
def d_nth(d, n):
    pointer = 'head'
    counter = 0
    L = [[0, None, pointer, d[pointer][1]]] 
    while d[pointer][1] != 'end':
        counter += 1
        tmp = [counter, pointer, d[pointer][1]]
        pointer = d[pointer][1]
        tmp.append(d[pointer][1])
        L.append(tmp)

    #del node, previous node to next node
    print(L)
    d[L[-n][1]][1] = L[-n][3]
    d.pop(L[-n][2], None)
    
    return d
    
    
    
pl(d_nth(d, 2))


# In[ ]:


#can also soved by two pointer always separated by n nodes

