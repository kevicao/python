#!/usr/bin/env python
# coding: utf-8

# Longest Substring Without Repeating Characters
# 
# input: "abcabcbb"
# <br>
# Output: 3 <br>
# Explanation: The answer is "abc", with the length of 3. 

# In[4]:
# scan left to right and track best result so far. if repeat, move starting index to the repeated one
def longestUniqueSubsttr(string): 

       

    # Creating a set to store the last positions of occurrence 

    seen = {} 
    maximum_length = 0 

    # starting the inital point of window to index 0 

    start = 0 
    for end in range(len(string)): 
        # Checking if we have already seen the element or not 
        if string[end] in seen: 
            # If we have seen the number, move the start pointer 

            # to position after the last occurrence 

            start = max(start, seen[string[end]] + 1) 

        # Updating the last seen value of the character 

        seen[string[end]] = end 

        maximum_length = max(maximum_length, end-start + 1) 

    return maximum_length 

# Driver Code 

string = "geeksforgeeks" 

print("The input string is", string) 

length = longestUniqueSubsttr(string) 

print("The length of the longest non-

#######
def longest_substring(s):
    #non-empty
    if len(s) == 0:
        return (0, '', 0)
    elif len(s) == 1:
        return (0, s, 1)
    else:
        pos = 0
        max_L = 1

        index = 0
        cur_L = 0
        sub = dict()
        while index < len(s) - 1:
            for high in range(index, len(s)):
                if s[high] in sub:
                    if cur_L > max_L:
                        pos = index
                        max_L = cur_L
                    #move index
                    for x in range(index, sub[s[high]] + 1):
                        sub.pop(s[x])
                    index = x + 1 
                    sub[s[high]] = high
                else:
                    sub[s[high]] = high
                    cur_L += 1 
        return (pos,s[pos:pos+max_L], max_L)
            
print(longest_substring('abcabcbb'))
print(longest_substring('bbbbb'))
print(longest_substring('ABDEFGABEF'))


# In[ ]:





# In[ ]:




