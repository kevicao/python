233. Number of Digit One


# https://codingforspeed.com/how-many-ones-between-number-1-to-n/

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0):
            return 0
        if (n < 10):         
            return 1

        count = 0    
        highest = n  
        weight = 1   
        while highest >= 10:  
            highest = highest//10
            weight = weight*10

        if (highest == 1):
            count = self.countDigitOne(weight - 1) + self.countDigitOne(n - weight) + n - weight + 1 
        else:
            count = highest * self.countDigitOne(weight - 1) + self.countDigitOne(n - highest * weight) + weight

        return count    

# https://leetcode.com/problems/number-of-digit-one/solution/


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        countr = 0
        i = 1
        while i <= n:
            divider = i * 10;
            countr += (n / divider) * i +  min(max(n % divider - i + 1, 0), i)
            i = i*10

        return countr 