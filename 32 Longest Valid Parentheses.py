loop#!/usr/bin/env python
# coding: utf-8

# In[18]:Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
https://baihuqian.github.io/2018-06-02-longest-valid-parentheses/

def lvp(L):
    bal = 0
    
    max_l = 0
    counter = 0
    last_val = -1
    for index, c in enumerate(L):
        if c == '(':
            bal += 1
        else:
            bal -= 1
            
        if bal > 0: 
            counter += 1
        if bal == 0:
            counter += 1
            if counter > max_l:
                max_l = counter
            last_val = index
            
        if bal < 0: 
            counter = 0
            bal = 0
            last_val = index
            
#         print(c, index, bal, counter, max_l)
#     print(bal)       
    if bal > 0: 
        tmp = len(L)-1 - last_val - bal
        if tmp > max_l:
            max_l = tmp
            
    print(max_l)
        
# lvp(')()())')       
# lvp('(()')  
# lvp('()((())')
lvp('())((())')


# In[9]:





# In[ ]:




