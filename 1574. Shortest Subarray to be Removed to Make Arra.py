1574. Shortest Subarray to be Removed to Make Array Sorted

# keep two pointers from both ends
# there are thress possibilities: remove from left, remove from right, and remove from middle
# when from middle, check all possible cases by sliding the windown

# https://www.geeksforgeeks.org/length-of-smallest-subarray-to-be-removed-such-that-the-remaining-array-is-sorted/

class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
        left = 0
        right = len(arr) - 1
        
        while left < right and arr[left + 1] >= arr[left]:
            left += 1
            
        if left == right:
            return 0
        
        while right > left and arr[right - 1] <= arr[right]:
            right -= 1
            
        mincount = min(len(arr) - left - 1, right)
                
        j = right
        for i in range(left+1):
            if arr[i] <= arr[j]:
                mincount = min(mincount, j-i - 1)
            elif j < len(arr) - 1:
                j += 1
            else:
                break
        return mincount
            
