1052. Grumpy Bookstore Owner


# sliding windown: do not need check all element in the windowns just the two changes

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        if grumpy[0] == 0:
            num = customers[0]
        else:
            num = 0
        
        extra = [0]*len(grumpy)
        for j in range(X):
            if j < len(grumpy) and grumpy[j] == 1:
                extra[0] += customers[j]
                
        for i in range(1, len(grumpy)):
            if grumpy[i] == 0:
                num += customers[i]
            temp = extra[i-1]
            if grumpy[i-1] == 1:
                temp -= customers[i-1]

            if i+X-1 < len(grumpy) and grumpy[i+X-1] == 1:
                temp += customers[i+X-1]

            extra[i] = temp
            
    
        return num +  + max(extra)
                    