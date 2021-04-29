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

# compass


# You are given two sorted lists of log messages (time stamp and message). Merge the two lists into a single list sorted by timestamp.

def merge_sorted_list(A, B):
    i = 0
    j = 0
    
    C = []
    while (i < len(A)) and (j < len(B)):
        if A[i] <= B[j]:
            C.append((A[i]))
            i = i + 1
            
        else:
            C.append(B[j])
            j += 1
            
    if i < len(A):
        C = C + A[i:]
                
    if j < len(B):
        C = C + B[j:]
                    
    return C
                     
# You are given a list of log messages(timestamp and message) that consists of several sorted blocks(sub arrays). Return the list sorted by the time stamp.

# Time Stamp Message
# 1            m_1
# 2             m_2   
# 5             m_3
                     
# 2             m_4                     
# 5             m_5
# 11            m_6
# 21            m_7
                     
# 4            m_8
# 9            m_9
# 112             m_10
# 1             m_10
                     
                     
                     
def find_sorted_list(arr):
    ans = []
                     
    tmp = []
    for i in range(len(arr) -1) :
        tmp.append(arr[i])
                     
        if arr[i] > arr[i+1] :
            ans.append(tmp)
            tmp = []
    
    tmp.append(arr[-1])
    ans.append(tmp)
                     
    return ans
                     

def merge_n_lists(arr):

    while len(arr) > 1:
        n = len(arr) 
        count = 0
        i = 0 
        while i < n-1 :
            arr.append(merge_sorted_list(arr[i], arr[i+1]))
            i += 2
            count += 1
        
        if i == n-1:
            arr.append(arr[i])
            count += 1
        
        arr = arr[-count:]
                     
    return arr[0]
                     
                     
a = [[1,2], [9,10,11], [5,6]]
a = [[], [9,10,11], [5,6]]
a = [[]] 
a = [1,2,9,10,11,5,6]
a = find_sorted_list(a)
print(a)
print(merge_n_lists(a) ) 


