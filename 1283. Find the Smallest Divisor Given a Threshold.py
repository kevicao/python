1283. Find the Smallest Divisor Given a Threshold


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
        compute_sum = lambda x: sum([((n-1)//x) + 1 for n in nums])
        
        l = 1
        r = max(nums)
        while l < r: 
            print()
            print(l,r)
            mid = (l + r)/2
            if compute_sum(mid) <= threshold:
                r = mid
            else:
                l = mid + 1
            print(mid, compute_sum(mid))
            print(l,r)
                
        return l