1569. Number of Ways to Reorder Array to Get Same BST

# We separate all the elements into two lists, depending on whether they are less than or more than the root. 
# Then we recurse on those left and right sublists. The combination is for the macro ordering 
# between left and right, and the recursive factors are for the internal ordering of left and right themselves. 
# I minus 1 from the result because we don't count the original ordering.

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(nums):
            def comb(n,r):
                import math
                f = math.factorial
                return f(n) / f(r) / f(n-r)

            if len(nums) <= 2: 
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            
            return comb(len(left)+len(right), len(right)) * f(left) * f(right)
        
        return (f(nums)-1) % (10**9+7)        