#!/usr/bin/env python
# coding: utf-8

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.

# In[19]:


L1 = [1,2]
L2 = [3] #2.5

#https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation

def median_two_array(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    if n1 < n2: return median_two_array(L2, L1)
    
    
    l = 0
    h = n2*2
    
    while l <= h:
        med2 = (l+h)//2
        med1 = n1 + n2 - med2
        
        l1 = float('-inf') if med1 == 0 else L1[(med1-1)//2]
        l2 = float('-inf') if med2 == 0 else L2[(med2-1)//2]
        r1 = float('inf') if med1 == n1*2 else L1[(med1)//2]
        r2 = float('inf') if med2 == n2*2 else L2[(med2)//2]
        
        if (l1 > r2):
            l = med2 + 1
        elif l2 > r1:
            h = med2 - 1
        else:
            return (max(l1,l2) + min(r1, r2)) / 2
            
    return -1
        
print(median_two_array(L1, L2) )       
    


#     l1  r1
# l   l2  r2    h  
# should: l1 < r2 and l2 < r1
# if l1 > r2: increase r2  --> position
# if l2 > r1: decrease l2 ---> decrease position

# In[1]:


3//2


# In[ ]:




