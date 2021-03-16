#!/usr/bin/env python
# coding: utf-8

# Example:
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) <br>
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# In[12]:


int1 = [0]
int2 = [5,6,4]

def add_two_number(int1, int2):
    if len(int1) >= len(int2):
        long = int1
        short = int2
    else:
        long = int2
        short = int1
        
    res = []
    carry = 0
    for index in range(0,len(short)):        
        res.append((short[index] + long[index] + carry)%10)
        carry = int((short[index] + long[index] + carry)/10)
    for index in range(len(short), len(long)):
        res.append((long[index] + carry)%10)
        carry = int((long[index] + carry)/10)
    
    return res 

add_two_number(int1,int2)


# In[14]:


20281.0/(20281+2627)


# In[ ]:




