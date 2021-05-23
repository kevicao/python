# 1143. Longest Common Subsequence

# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

class Solution(object):
    def longestCommonSubsequence(self, X, Y):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # find the length of the strings
        m = len(X)
        n = len(Y)

        # declaring the array for storing the dp values
        L = [[None]*(n+1) for i in xrange(m+1)]

        """Following steps build L[m+1][n+1] in bottom up fashion
        Note: L[i][j] contains length of LCS of X[0..i-1]
        and Y[0..j-1]"""
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0 :
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j] , L[i][j-1])

        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        return L[m][n]
    #end of function lcs 


# TLE
class Solution(object):
    def longestCommonSubsequence(self, X, Y):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(X)
        n = len(Y)
  
        if m == 0 or n == 0:
            return 0;
        elif X[m-1] == Y[n-1]:
            return 1 + self.longestCommonSubsequence(X[:-1], Y[:-1])
        else:
            return max(self.longestCommonSubsequence(X, Y[:-1]), 
                       self.longestCommonSubsequence(X[:-1], Y))   