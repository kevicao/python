1793. Maximum Score of a Good Subarray


# one pass with two pointer

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        result = m = nums[k]
        i = j = k
        while i > 0 or j < n - 1:
            if i == 0:
                while j < n:
                    m = min(m, nums[j])
                    result = max(result, m * (j - i + 1))
                    j += 1
                break
            if j == n - 1:
                while i >= 0:
                    m = min(m, nums[i])
                    result = max(result, m * (j - i + 1))
                    i -= 1
                break
            if nums[i - 1] < nums[j + 1]:
                j += 1
                m = min(m, nums[j])
            else:
                i -= 1
                m = min(m, nums[i])
                
            result = max(result, m * (j - i + 1))
            
        return result



# double loop
# too slow


class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minM = [[0]*len(nums) for x in nums]
        
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):                
                temp = min(temp, nums[j])
                minM[i][j] = temp
                
        score = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i <= k and j>=k:
                    score = max(score, minM[i][j]*(j-i+1))
                    if score == 21:
                        print(i,j)
         
        return score
    
