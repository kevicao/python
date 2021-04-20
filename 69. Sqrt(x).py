69. Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
            
        left = 0
        right = x
        while left <= right:
            mid = (left + right)//2
            
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid + 1
                ans = mid
            else:
                right = mid -1
        return ans

#too slow

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            rturn x
            
        left = 0
        right = x
        while left < right-1:
            mid = (left + right)//2
            
            if mid*mid > x and (mid-1)*(mid-1) <= x:
                return mid-1
            elif mid*mid <=x and (mid+1)*(mid+1) > x:
                    return mid
            
            elif mid*mid > x:
                right -= 1
            elif mid*mid <= x:
                left = mid
                
        if right*right <= x:
            return right
        else:
            return left