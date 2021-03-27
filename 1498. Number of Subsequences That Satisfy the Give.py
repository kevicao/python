1498. Number of Subsequences That Satisfy the Given Sum Condition



class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        result = 0
        
        while i <= j:
            if nums[i] + nums[j] <= target:
                result += 2 ** (j - i)
                i += 1
            else:
                j -= 1
        return result % (10 ** 9 + 7)
                