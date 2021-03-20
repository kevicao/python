#!/usr/bin/env python
# coding: utf-8

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

# In[ ]:


# def regex(s,p):
    


# In[8]:


#If a star is present in the pattern, it will be in the second position 
#\text{pattern[1]}pattern[1]. Then, we may ignore this part of the pattern, or 
#delete a matching character in the text. If we have a match on the remaining strings 
#after any of these operations, then the initial inputs matched.
def regex(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (regex(text, pattern[2:]) or
                first_match and regex(text[1:], pattern))
    else:
        return first_match and regex(text[1:], pattern[1:])
    


# In[9]:


#test 
print(regex('aa', 'a')) #false
print(regex('aa', 'a*')) #true
print(regex('ab', '.*')) #true
print(regex('aab', 'c*a*b')) #true
print(regex('mississippi', 'mis*is*p*.')) #false


# In[ ]: the following is too slow

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if len(s) == len(p) == 0:
            return True
        
        if len(p) == 0:
            return False
        
        if len(s) == 0:
            if len(p) == 1:
                return False
            while len(p) >= 2:
                if p[1] != '*':
                    return False
                else:
                    return self.isMatch(s,p[2:])
        if len(p) == 1:
            print('here')
            if len(s) > 1:
                return False
            elif p[0] == s[0] or p[0] == '.':
                return True
            else:
                return False

        if p[1] != '*':
            if p[0] == '.' or p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return False 
            
        else:
            if p[0] == '.' or p[0] == s[0]:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
            
        



