75. Sort Colors

# only one pass
# use i,j to label two ends, and use k to travel

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = k = 0
        j = len(nums) - 1
        
        while k<=j:
            print(i,j,k)
            if nums[k] == 1:
                k += 1
            elif nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                    
            
