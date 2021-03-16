#!/usr/bin/env python
# coding: utf-8

#. https://leetcode.com/problems/combination-sum-ii/solution/

# In[10]:leetcode 39: Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input
 http://yucoding.blogspot.com/2012/12/leetcode-question-16-combination-sum.html


def search(candidates, target, i, res, ress):
    if target < 0:
        return
    else:
        if target == 0:
            res.append(ress[:]) #It is important to use "ress[:]" instead of "ress"
        else:
            while i < len(candidates) and target-candidates[i] >= 0:
                ress.append(candidates[i])
                search(candidates, target-candidates[i], i, res, ress)
                i += 1
                ress.pop(-1) #if use "ress", this will pop the elemtnes in res also

# @param {integer[]} candidates
# @param {integer} target
# @return {integer[][]}
def combinationSum(candidates, target):
    res =[]
    ress = []
    search(sorted(candidates), target, 0, res, ress)
    return res


combinationSum([2,3,6,7], 7)    


# In[6]:


a = [2,2,3]
a.pop(-1)
a


# In[ ]: 40. Combination Sum II. candidates only use once




