1340. Jump Game V

#check each position, for each of them, check all possible jump, but save them in DP
#dynamic programming

class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        def jump(i):
            if visited[i]:
                return dp[i]
            else:
                visited[i] = 1

                j = i-1
                while max(0, i-d) <= j and arr[j] < arr[i]:
                    dp[i], j = max(dp[i], jump(j)+1), j-1

                j = i+1
                while j <= min(len(arr)-1, i+d) and arr[j] < arr[i]:
                    dp[i], j = max(dp[i], jump(j)+1), j+1

                return dp[i]
        
        n, ans = len(arr), 0     
        dp, visited = [1 for _ in range(n)], [0 for _ in range(n)]
        
        for i in range(n):
            ans = max(ans, jump(i))
        
        return ans 


# 1696. Jump Game VI
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Keep track of the largest and the second largest value of the last k dp values
        # dp[i] to track the largest sum to reach i from 0
        # l Keep track of the largest and r keep track of the second largest value on the right of l 
#         of the last k dp values
# r is always on the right of l 
        dp = [0] * len(nums)
        l = r = 0
        
        for i in range(len(nums)):
            if i > l + k:
                l, r = r, r + 1
            dp[i] = dp[l] + nums[i]
            if dp[i] >= dp[l]:
                l, r = i, i + 1
            elif dp[i] >= dp[r]:
                r = i
                
        print(dp)
        return dp[-1]   

# the following one will exceed time limit. it scan k value for each i from right

class Solution(object):
    def checkIfPrerequisite(self, nums, k):

        dp = [0]*len(nums)
        dp[-1] = nums[-1]
        
        for i in range(len(nums)-2, -1, -1):
            j = i+1
            tmp = -float('inf')
            while j <= min(len(nums)-1, i+k):
                tmp, j = max(tmp, nums[i] + dp[j]), j+1     
            dp[i] = tmp
        
        print(dp)
        return dp[0] 
    
a = Solution()
a.checkIfPrerequisite([1,-1,-2,4,-7,3], 2)