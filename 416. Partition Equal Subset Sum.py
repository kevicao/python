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



# facebook: Balanced Split
# Given an array of integers (which may include repeated integers), determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same, and all of the integers in A are strictly smaller than all of the integers in B.
# Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

#based on quicksort

def balancedSplitExists(arr):
    if not arr:
        return False
    
    target = sum(arr)
    if target % 2 != 0:
        return False
    
    target /= 2

    def canSplit(cur_arr, lo_sum):
        if not cur_arr:
            return False
        
        pivot = cur_arr[0]
        s, lo, hi = 0, [], []
        for x in cur_arr:
            if x < pivot:
                s += x
                lo.append(x)
            elif x == pivot:
                s += x
            else:
                hi.append(x)
                
        if target == s + lo_sum:
            return True
        elif s < target:
            return canSplit(hi, s + lo_sum)
        else:
            return canSplit(lo, lo_sum)
        
    return canSplit(arr, 0)



tests = [
        [[1, 5, 7, 1], True],
        [[12, 7, 6, 7, 6], False],
        [[], False],
        [[2], False],
        [[20, 2], False],
        [[5,7,20,12,5,7,6,14,5,5,6], True],
        [[5,7,20,12,5,7,6,7,14,5,5,6], False],
        [[1,1,1,1,1,1,1,1,1,1,1,1], False]
        ]
for test, ans in tests:
    print(balancedSplitExists(test) == ans)