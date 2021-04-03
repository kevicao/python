1011. Capacity To Ship Packages Within D Days


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        
        l = max(weights)
        r = sum(weights)
        
        while l < r:
            m = (l + r)//2
            s, count = 0, 1
            for weight in weights:
                s += weight
                if s > m:
                    s = weight
                    count += 1
            if count > D:
                l = m + 1
            else:
                r = m
        return l
        
        