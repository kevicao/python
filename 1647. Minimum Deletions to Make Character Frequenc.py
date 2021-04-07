1647. Minimum Deletions to Make Character Frequencies Unique



class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(c1.values())
        
        largest = max(c2)
        ans = 0
        
        while(largest>0):
            if largest in c2 and c2[largest]>1:
                ans+=c2[largest]-1
                c2[largest-1] = c2.get(largest-1,0)+c2[largest]-1
                
            largest-=1
            
        return ans

      