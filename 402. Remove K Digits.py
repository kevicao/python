402. Remove K Digits

#from left, find the first number that is bigger than next and remove it

#or if we still have m digits to remove, we can find the min of left m digits and keep it


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        s = 0
        e = k
         
        res = ''
        flag = True
        
        while s < len(num) and e < len(num):
            m = num[s]
            for i in range(s+1,e+1):
                if num[i] < m:
                    m = num[i]
                    s = i
            s +=1
            e += 1
            if flag:
                if m != '0':
                    res += m
                    flag = False
            else:
                res += m
        
            
        return res if len(res) > 0 else '0'

