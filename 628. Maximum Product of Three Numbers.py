628. Maximum Product of Three Numbers


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')
        
        for n in nums:
            if n <= min1:
                min2 = min1;
                min1 = n
            elif (n <= min2): 
                min2 = n

            if (n >= max1):
                max3 = max2
                max2 = max1
                max1 = n
            elif (n >= max2):
                max3 = max2
                max2 = n
            elif (n >= max3):
                max3 = n

        return max(min1 * min2 * max1, max1 * max2 * max3);


# Largest Triple Products
# You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
# Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.

#what about negative numbers
def findMaxProduct(arr):
  # Write your code here
    ans = [-1, -1]
    ans.append(arr[0]* arr[1]* arr[2])
    top3 = sorted(arr[:3])
    
    for i in range(3, len(arr)):

        if arr[i] >= top3[2]:
            top3.pop(0)
            top3.append(arr[i])
        elif arr[i] >= top3[1]:
            top3.pop(0)
            top3.insert(1,arr[i])
        elif arr[i] >= top3[0]:
            top3.pop(0)
            top3.insert(0,arr[i]) 
        ans.append(top3[0]*top3[1]*top3[2])
        
    return ans 