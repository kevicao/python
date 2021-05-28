#!/usr/bin/env python
# coding: utf-8

# # what is the difference of recusion and itteration
# #递归, recursive, funtion calls itself
# #迭代, itterative

# In[14]:


def fab_recursion(index):
    if index == 1 or index == 2:
        return 1
    else:
        return fab_recursion(index-1) + fab_recursion(index-2)
    
print(fab_recursion(10))


# In[13]:


def fab_iteration(index):
    if index == 1 or index == 2:
        return 1
    else:
        f1 = 1
        f2 = 1
        for i in range(3, index+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            
        return f3
    
fab_iteration(10)


# # 46. Permutations

# https://www.cnblogs.com/grandyang/p/4358848.html

# In[1]:



#this is recursion solution
def pm_recursion(L):
    res = []
    out = []
    
    visited = [0]*len(L)
    
    permuteDFS(L, 0, visited, out, res)
    
    return res

def permuteDFS(num, level, visited, out, res):
    if level == len(num):
        res.append(out[:])
        
        return
    
    for i in range(len(num)):
    
        if visited[i] == 1: 
            continue
        
        visited[i] = 1        
        out.append(num[i])
        print(out)
        
        permuteDFS(num, level + 1, visited, out, res);
        out.pop()
        
        visited[i] = 0
        
pm_recursion([1,2,3])


# In[44]:


#in above, level just tells us we are done or not, we can do this by checking length using len
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        out = []

        visited = [0]*len(nums)

        self.permuteDFS(nums, visited, out, res)

        return res

    def permuteDFS(self, num, visited, out, res):
        if len(out) == len(num):
            res.append(out[:])

            # return #can have this line

        for i in range(len(num)):

            if visited[i] == 1: 
                continue

            visited[i] = 1        
            out.append(num[i])

            self.permuteDFS(num, visited, out, res);
            out.pop()

            visited[i] = 0   
        
pm_recursion([1,2,3])

#in above we use visited to mark number used so we need pop, we can pass remaining numbers only so that we do not need visited
#because we are not appending out inside the function but only in calls, we do not need pop in the function
def generate_graph(result, curr_num, next_num):
  if not next_num:
    result[tuple(curr_num)] = []
    
  for i in range(len(next_num)):
    generate_graph(result, curr_num+[next_num[i]], next_num[:i]+next_num[i+1:])

# # deal with one number a time
# 当n=1时，数组中只有一个数a1，其全排列只有一种，即为a1
# 
# 当n=2时，数组中此时有a1a2，其全排列有两种，a1a2和a2a1，那么此时我们考虑和上面那种情况的关系，我们发现，其实就是在a1的前后两个位置分别加入了a2

# ### permutations

# In[39]:


# still leetcode 46
#this is itteration soltuion
def pm(L):
    res = [[L[0]]]
    
    for x in L[1:]: #add a new number each time
        tmp_res = []
        for l in res:
            for i in range(len(l)+1): #add at each position
                
                l.insert(i,x)
                tmp_res.append(l[:])
                l.pop(i) #get back original list

        res = tmp_res[:]
        
    return res   
    
pm([1,2,3])


# ### 78 subsets

# ### 17_Letter_Combinations_of_Phone_Number

# In[ ]:


#each additon number will add each letter to all solutions so far
#[a,b,c]
#[ad, bd, cd], and .....
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.d = {2:['a', 'b', 'c'],
         3:['d', 'e', 'f'],
         4:['g', 'h', 'i'],
         5:['j', 'k', 'l'],
         6:['m', 'n', 'o'],
         7:['p', 'q', 'r', 's'],
         8:['t', 'u', 'v'],
         9:['w', 'x', 'y', 'z']
        }
        
        if len(digits) == 0:
            return [] 
        
        cb = self.d[int(digits[0])]
        
        for index, n in enumerate(digits[1:]):
            tmp = []
            for l in self.d[int(n)]:
                tmp = tmp + [x + l for x in cb]
            cb = tmp[:]

        return cb     


# In[ ]:


# recursive, still use above observation
class Solution(object):
    def letterCombinations(self, L):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.d = {2:['a', 'b', 'c'],
         3:['d', 'e', 'f'],
         4:['g', 'h', 'i'],
         5:['j', 'k', 'l'],
         6:['m', 'n', 'o'],
         7:['p', 'q', 'r', 's'],
         8:['t', 'u', 'v'],
         9:['w', 'x', 'y', 'z']
        }
        
        if len(L) == 0:
            return []
        elif len(L) == 1:
             return self.d[int(L[0])]
        else:
            tmp = []
            for l in self.d[int(L[-1])]:
                tmp = tmp + [x + l for x in self.letterCombinations(L[:-1])]
            return tmp  

