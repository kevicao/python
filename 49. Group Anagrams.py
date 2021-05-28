#!/usr/bin/env python
# coding: utf-8

# In[1]:Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
            
        return ans.values()      

# In[2]:


#build a diction of arrays, key is the count of letters, couter size is 26

# facebook phone interview: Counting Triangles
# Given a list of N triangles with integer side lengths, determine how many different triangles there are. Two triangles are considered to be the same if they can both be placed on the plane such that their vertices occupy exactly the same three points.

#this becomes n*log(n) while above is n

def countDistinctTriangles(arr):
  # Write your code here
    arr = [sorted(x) for x in arr]
    arr = sorted(arr, key=lambda x: x[0])
    
    count = 1
    l = 0
    for i in range(1,len(arr)):
        if arr[i][0] == arr[l][0] and arr[i][1] == arr[l][1] and arr[i][2] == arr[l][2]:
            continue
        else:
            l =i
            count += 1
    return count  


#facebook practice: Balance Brackets
# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# We consider two brackets to be matching if the first element is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type, e.g., ( and ), [ and ], and { and } are the only pairs of matching brackets.
# Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
# The sequence is empty, or
# The sequence is composed of two, non-empty, sequences both of which are balanced, or
# The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
# You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false
def isBalanced(s):
    q = []
    l = ['(', '[', '{']
    r = [')', ']', '}']
    h = {')':'(', '}':'{', ']':'['}
    for x in s:
        if x in l:
            q.append(x)
        elif x in r:
            if  q and (h[x] == q[-1]):
                q.pop(-1)
            else:
                return False
                
        else:
            return False
        
    if q:
        return False
    else:
        return True  # Write your code here