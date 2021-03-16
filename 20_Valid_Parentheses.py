#!/usr/bin/env python
# coding: utf-8

# In[4]: stack: push and pop whrn match


def val_p(s):
    L = []
    openp = ['(', '[', '{']
    close = [')', ']', '}']
    
    d = {'(':')', '[':']', '{':'}'}
    
    if len(s) == 0:
        return True
    
    for index, x in enumerate(s):
        if x in openp:
            if index == len(s) - 1:
                return False
            else:
                L.append(x)
                
        if x in close:
            if len(L) == 0:
                return False
            else:
                if x == d[L[-1]]:
                    L.pop()
                else:
                    return False
    if len(L) == 0:
        return True
    else:
        return False
    
print(val_p('()[]{}')) #true
print(val_p('([)]')) #false
print(val_p('')) #true
print(val_p('{[]}')) #true
            


# In[ ]:




