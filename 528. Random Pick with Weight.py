528. Random Pick with Weight



class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        

    def pickIndex(self):
        """
        :rtype: int
        """
        
        if len(self.w) ==1:
            return 0
        
        acc = [self.w[0]]
        for i in range(1,len(self.w)):
            acc.append(acc[i-1] + self.w[i])
        
        import random
        import bisect

        return bisect.bisect(acc, random.uniform(0,acc[-1]) )
        
       



build long array; pass time limit

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        

    def pickIndex(self):
        """
        :rtype: int
        """
        
        if len(self.w) ==1:
            return 0
        
        acc = []
        for i in range(len(self.w)):
            acc = acc + [i]*self.w[i]
        
        import random
        
        ind = int(random.uniform(0,len(acc)))

        return acc[ind]
        