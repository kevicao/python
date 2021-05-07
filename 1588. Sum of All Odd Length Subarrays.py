1588. Sum of All Odd Length Subarrays

# https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(arr)):
            ans += arr[i]*(((i+1)*(len(arr) - i) + 1)//2)
            
        return ans


# Sum of all Subarrays
# https://www.geeksforgeeks.org/sum-of-all-subarrays/
