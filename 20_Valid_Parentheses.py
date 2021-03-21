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

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        p = []
        
        for x in s:
            if len(p) == 0 or x in ['(', '{', '[']:
                p.append(x)
            elif x == ')':
                if p[-1] != '(':
                    return False
                else:
                    p.pop(-1) 
                    
            elif x == ']':
                if p[-1] != '[':
                    return False
                else:
                    p.pop(-1)
            elif x == '}':
                if p[-1] != '{':
                    return False
                else:
                    p.pop(-1)  
                    
        return len(p) == 0


