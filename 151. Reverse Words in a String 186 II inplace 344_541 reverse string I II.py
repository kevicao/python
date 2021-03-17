#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#344 is just reverse a string

#inplace solution
#reverse each word first
#reverse whole string 
#151 reverse words in a string, remove extra space; same as 186 but no extra space which is simplier
class Solution(object):
    def reverse(self, s):
        s = list(s)
        l = len(s)
        m = len(s)//2
        for i in range(m):
            t = s[i]
            s[i] = s[l-i-1]
            s[l-i-1] = t
        return ''.join(s)
        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        L = s.split(' ')
        L = [x for x in L if len(x) > 0]

        for i in range(len(L)):
            L[i] = self.reverse(L[i])
        
        return self.reverse(' '.join(L))

# In[9]:


#541 reverse first k for every k

def reverse_k(L, k):
    i = 0
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        while i < len(L):           
            j = min(i+k-1, len(L))
            L = reverse(L, i, j)
            i = i+2*k
    return L
            
def reverse(L, i, j):
    while i < j:
        tmp = L[i]
        L[i] = L[j]
        L[j] = tmp
        i += 1
        j -= 1
        
    return L
L = ["a","b","c","d","e","f","g"]
k = 2  #"bacdfeg"
print(reverse_k(L,2))


# In[ ]:




