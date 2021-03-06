#!/usr/bin/env python
# coding: utf-8

# In[22]:Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum


#https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
def max_subarray(L):
    if len(L) == 1:
        return L[0]
    elif len(L) == 0:
        return -10000   
    else: 
        print(L)
        mid = len(L)//2
        left = max_subarray(L[:mid])
        right = max_subarray(L[mid:])
        #cross 
        sm = 0
        left_sum = -10000
        for i in range(mid, -1, -1) : 
            sm = sm + L[i] 
            if (sm > left_sum) : 
                left_sum = sm        
        
        # Include elements on right of mid 
        sm = 0; right_sum = -1000
        for i in range(mid + 1, len(L)) : 
            sm = sm + L[i] 

            if (sm > right_sum) : 
                right_sum = sm 
                
        # Return sum of elements on left and right of mid 
        
        return max(left_sum + right_sum, left, right)      
            
        
max_subarray([-2,1,-3,4,-1,2,1,-5,4])   
# max_subarray([2, 3, 4, 5, 7]) 

# Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = dp[0]

        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i - 1]
            result = max(result, dp[i])

        return result
# In[13]:


# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        print(L)
        print(R)
        print('arr is', arr)
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
            
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
  


# # max product subarray

# In[4]:



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dpmin = [1]*len(nums)
        dpmax = [1]*len(nums)
        dpmin[0] = nums[0]
        dpmax[0] = nums[0]
        
        result = dpmax[0]

        for i in range(1, len(nums)):
            print(i)
            temp = dpmax[i-1]
            dpmax[i] = max(max(dpmin[i-1]*nums[i], dpmax[i-1]*nums[i]), nums[i])
            dpmin[i] = min(min(dpmin[i-1]*nums[i], temp*nums[i]), nums[i])

            result = max(result, dpmax[i])

        return result        






