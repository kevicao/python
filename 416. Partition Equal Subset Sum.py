416. Partition Equal Subset Sum

# https://leetcode.com/problems/partition-equal-subset-sum/discuss/1171558/Python-4-lines!
# suppose we have two groups, and dp has the possible difference of sum between the two, sum(a) - sum(b)
# each time we have a new element, we can add to a or b, which 

# suma - sumb = dp
# suma - sumb - num = newdp

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = {0}
        for num in nums:
            dp = {i - num for i in dp} | {num + i for i in dp} 
        return 0 in dp

