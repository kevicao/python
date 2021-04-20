62. Unique Paths

#find path from top left to bottom right of matrix
#dynamic programming

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        List = [[1]*n]*m
        
        for i in range(1,m):
            for j in range(1,n):
                List[i][j] = List[i][j-1] + List[i-1][j]
        print(List)        
        return List[m-1][n-1]