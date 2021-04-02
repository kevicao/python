283. Move Zeroes

zeros order does not matter

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l] = nums[i]
                l += 1
                
        for i in range(l, len(nums)):
            nums[i] = 0


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        r = len(nums) 
        for i in range(len(nums) - 1, -1, -1):
                
            if nums[i] == 0:
                for j in  range(i+1, r):
                    nums[j-1], nums[j] = nums[j], nums[j-1]

                r -= 1