# backtracking to find all subset of nums list (leetcode 78)

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

# binary search leetcode 69

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
            
        left = 0
        right = x
        while left <= right:
            mid = (left + right)//2
            
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid + 1
                ans = mid
            else:
                right = mid -1
        return ans