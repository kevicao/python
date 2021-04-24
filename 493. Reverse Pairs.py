493. Reverse Pairs

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls, count = [], 0
        
        for i in range(len(nums) - 1, -1, -1):
            j = bisect.bisect_left(ls, nums[i])
            count += j
            bisect.insort(ls, 2 * nums[i])
        return count 