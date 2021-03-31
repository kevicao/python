875. Koko Eating Bananas

binary search

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """        
        
        
        def possible(K):
            return sum((p-1) / K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) / 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo