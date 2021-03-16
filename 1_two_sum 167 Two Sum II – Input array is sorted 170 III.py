#!/usr/bin/env python
# coding: utf-8

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# In[15]:


List = [2, 7, 11, 15]
target = 26
# use sum - value1 as key
def two_sum(List, target):
    d = dict()
    for index in range(0, len(List)):
        if List[index] in d.keys():
            result = [index, d[List[index]]]
            result.sort()
            print(result)
            print(1)
        else: 
            d[target - List[index]] = index
            print(2)

two_sum([2, 7, 11, 15], 26)
# ### II
# 
# 167. Two Sum II - Input array is sorted
# 
# two pointers from both ends

# ### III
# 
# 170 Two Sum III - Data structure design
# 
# Design and implement a TwoSum class. It should support the following operations:add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
# 
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

# In[1]:


# same as I, there could be duplicate elements. use dict to store freqency


# In[ ]:




