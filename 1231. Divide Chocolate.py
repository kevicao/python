1231. Divide Chocolate

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

class Solution(object):
    def maximizeSweetness(self, nums, m):
        m  += 1
        l = float('inf')
        r = 0

        for n in nums:
            r += n
            l = min(l, n)

        def canSplit(nums, m, target):
            s = 0
            cnt = 0

            for n in nums: 
                if s + n >= target:
                    s = 0
                    cnt += 1
                else:
                    s += n

            return cnt >= m
            
            
        while(l+1 < r):
            print(l,r)
            mid = l + (r-l) // 2
            if canSplit(nums, m, mid):
                l = mid
            else:
                r = mid - 1

        if canSplit(nums, m, r):
            return r
        else:
            return l
    

a = Solution()
print(a.maximizeSweetness([1,2,2,1,2,2,1,2,2], 2))