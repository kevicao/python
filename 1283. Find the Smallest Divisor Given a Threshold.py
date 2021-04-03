1283. Find the Smallest Divisor Given a Threshold

# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
        compute_sum = lambda x: sum([((n-1)//x) + 1 for n in nums])
        
        l = 1
        r = max(nums)
        while l < r: 
            mid = (l + r)//2
            if compute_sum(mid) <= threshold:
                r = mid
            else:
                l = mid + 1
                
        return l