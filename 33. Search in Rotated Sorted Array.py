#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right)//2
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[left]: #left is sorted
                if nums[left] <= target and nums[m] > target:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if nums[m] < target and nums[right] >= target:
                    left = m+1
                else:
                    right = m - 1
        return -1
             
# In[32]:Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).


def sra(L, first, n):
#     print(L, first, n)
    if len(L) == 1:
        if L[0] == n:
            return first
        else:
            return -1
        
    elif len(L) == 0:
        return -1
    
    elif len(L) == 2:
        if L[0] == n:
            return first
        elif L[1] == n:
            return first + 1
        else:
            return -1
       
    else:
        m = int(len(L)/2)
        if L[0] <= L[m-1]:
            if n >= L[0] and n <= L[m-1]:
                return sra(L[:m], first, n)
            else: 
                return sra(L[m:], first + m, n)
            
        else:
            if n >= L[m] and n <= L[-1]:
                return sra(L[m:], first+m, n)
            else:
                return sra(L[:m], first, n)
                
                
print(sra([4,5,6,7,0,1,2], 0, 0))
print(sra([4,5,6,7,0,1,2], 0, 3))


# In[26]:


def factorial(num):
    print(num)
    if (num == 0 | num == 1):
        return 1
    else:
        return factorial(num - 1)
    
factorial(3)


# In[ ]
pushpraj.shukla@microsoft.com:




