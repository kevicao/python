78. Subsets

#  Given an integer array nums of unique elements, return all possible subsets (the power set).
# https://leetcode.com/problems/subsets/solution/

# cascading: add one number each time

 class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = [[]]
        
        
        for x in nums:
            tmp = []
            for y in ans:
                tmp += [y + [x]]
            
            ans = ans + tmp
            
        return ans
        
        
# backtracking

class Solution(object):
	def subsets(self, nums):
	    def backtrack(first = 0, curr = []):
	        # if the combination is done
	        if len(curr) == k:  
	            output.append(curr[:])
	            return
	        for i in range(first, n):
	            # add nums[i] into the current combination
	            curr.append(nums[i])
	            # use next integers to complete the combination
	            backtrack(i + 1, curr)
	            # backtrack
	            curr.pop()
	    
	    output = []
	    n = len(nums)
	    
	    for k in range(n + 1):
	        backtrack()
	        
	    return output


# bit operation

class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output