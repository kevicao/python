#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

L1 = [1,2,4]
L2 = [1,3,4, 10]

def merge(L1, L2):
    short = min( len(L1), len(L2))
    
    res = []
    l1 = 0
    l2 = 0
    while l1 < len(L1) and l2 < len(L2):
        if L1[l1] > L2[l2]:
            res.append(L2[l2])
            l2 += 1
        else:
            res.append(L1[l1])
            l1 += 1
            
    while l1 < len(L1):
        res.append(L1[l1])
        l1 += 1
    while l2 < len(L2):
        res.append(L2[l2])
        l2 += 1
        
    return res

merge(L1, L2)
        


# #merge k lsit
# 
# #https://leetcode.com/problems/merge-k-sorted-lists/solution/
# 
# 1. sort the total list nlogn
# 2. find smallest value among k each time, nlogk, wihtout priority queue kn   
#   #h = [], heappush/pop(h, (key, value))
#   
# 3. convert to merge 2 list, that is to merge one by one, kn
# 4. 
# 
# 
# 

# #
# Merge two arrays remove duplicates, report duplicates and print in sorted order

# In[ ]:


# In[14]:


def merge_k(L):
    
    if len(L) == 0:
        return []
    
    tracking = [0]*len(L)
    
    final = []
    while len(L) > 0:
        smallest = find_s([L[j][tracking[j]] for j in range(len(L))])
        final.append(L[smallest][tracking[smallest]])
        
        if tracking[smallest] + 1 < len(L[smallest]):
            tracking[smallest] += 1
        else:
            L.pop(smallest)
            tracking.pop(smallest)
            
    print(final)
        
        
    
def find_s(List):
    smallest = 0
    for i in range(1,len(List)):
        if List[i] < List[smallest]:
            smallest = i
    return smallest
        
merge_k([[1,4,5], [1,3,4], [2,6]])        


# In[ ]:




