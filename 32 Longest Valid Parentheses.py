#!/usr/bin/env python
# coding: utf-8

# https://leetcode.com/problems/longest-valid-parentheses/submissions/

class Solution(object):
    def longestValidParentheses(self, string):
        """
        :type s: str
        :rtype: int
        """

        maxans = 0
        dp = [0]*len(string)
        
        for i in range(1, len(string)):
            if string[i] == ')':
                if string[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                    
                elif (i - dp[i - 1] > 0) and string[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + ( dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2;
                
                maxans = max(maxans, dp[i]);

        return maxans


class Solution(object):
    def longestValidParentheses(self, string):
        """
        :type s: str
        :rtype: int
        """

        maxans = 0;
        stack = []
        stack.append(-1)
        
        for i in range(len(string)):
            if string[i] == '(':
                stack.append(i)
            else:
                stack.pop(-1);
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])

        return maxans


class Solution(object):
    def longestValidParentheses(self, string):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        maxlength = 0
        
        for i in range(len(string)):
            if string[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
            
        
        left = right = 0;
        for i in range(len(string) - 1, -1, -1): 
            if string[i] == '(':
                left += 1
            else: 
                right += 1
            
            if (left == right):
                maxlength = max(maxlength, 2 * left);
            elif (left > right): 
                left = right = 0;

        return maxlength;


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


# In[9]: facebook, give a string with (), you can delete character, find the longest balanced string
    
    # string '()'
    # '(a(b)' -> '(ab)' or 'a(b)'
    # '(a(bcd)cdf' -> '(abcd)' or 'a(bcd)'
    # ')(' -> ''
    # '(a))b(c)('
    
    
def find_longest_balanced_string(string):
    stack = []
    deleted =[]
    
    for i, s in enumerate(string):
        if s == '(':
            stack.append(i)
        elif s == ')':
            if stack:
                    stack.pop(-1)
            else:
                deleted.append(i)
    
    
    deleted = deleted + stack
    #convert to dic to find i fast
        
    ans =''      
    for i, s in enumerate(string):
        if i not in deleted:
            ans = ans + s
            
    return ans

print(find_longest_balanced_string('(a))b(c)('))
print(find_longest_balanced_string('(a(bcd)cdf'))




# In[ ]:




