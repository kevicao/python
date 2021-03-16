#!/usr/bin/env python
# coding: utf-8

# In[10]:


def ITR(n):
    units = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    mapping = {1000: 'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 
               50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    exceptions = [4,9,40,90, 400, 900]
    
    res = ''
    i = 0
    while i < len(units) and n > 0:
        integer = n//units[i]
        n = n%units[i]
        
        res += mapping[units[i]]*integer
        i += 1
        
    return res

print(ITR(3)) #"III"
print(ITR(4)) #"IV"
print(ITR(9)) #"IX"
print(ITR(58)) #"LVIII"
print(ITR(1994)) #"MCMXCIV"
print(ITR(41)) #XLI
        


# In[4]:


5//2


# In[6]:


'i'*3 + 'b'


# In[ ]:




