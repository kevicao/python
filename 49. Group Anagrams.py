#!/usr/bin/env python
# coding: utf-8

# In[1]:Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



input = ["eat", "tea", "tan", "ate", "nat", "bat"],
Output = [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]


# In[2]:


#build a diction of arrays, key is the count of letters, couter size is 26


# In[3]:


d = dict()
d[tuple('ate')] = []
d


# In[4]:


tuple('ate') == tuple('aet')


# In[ ]:




