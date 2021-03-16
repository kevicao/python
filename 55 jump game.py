#!/usr/bin/env python
# coding: utf-8

# In[12]:Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.



def canJumpFromPosition(position, nums):
    if position == len(nums) - 1:
        return True;

    furthestJump = min(position + nums[position], len(nums) - 1)
    for nextPosition in range(position+1, furthestJump+1):
        if canJumpFromPosition(nextPosition, nums):
            return True;

    return False;

canJumpFromPosition(0, [2,3,1,1,4])
canJumpFromPosition(0, [3,2,1,0,4])


# In[15]:


def jg_dp(nums):
    mem = [False]*len(nums)
    mem[-1] = 1
    for i in range(len(nums)-2, -1, -1):
        fur = min(nums[i] + i, len(nums)-1)
        for j in range(i+1, fur+1):
            if mem[j] == True:
                mem[i] = True
                break
    return mem[0]

jg_dp([3,2,1,0,4])


# In[ ]:




