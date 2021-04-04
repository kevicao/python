50. Pow(x, n)


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
            
        if n == 0:
            return 1
            
        if n == 1:
            return x
        
        mid = n//2
        if n%2 == 0:
            return self.myPow(x,n//2)**2
        else:
            return self.myPow(x, n//2)**2*x