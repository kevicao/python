774. Minimize Max Distance to Gas Station 

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized
can not add one in the middle of biggest gap since ideal may be add two in the gao to get 1/3 gap

class Solution(object):
    def minmaxGasDist(self, stations, K):
        left = 0
        right = 1e8

        def helper(stations, K, mid):
            cnt = 0
            n = len(stations)

            for i in range(len(stations) - 1):
                cnt += (stations[i + 1] - stations[i]) // mid

            return cnt <= K
        
        while right - left > 1e-6:
            mid = left + (right - left) / 2
            if helper(stations, K, mid):
                right = mid
            else :
                left = mid
        
        return left
    

 

a = Solution()
print(a.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))