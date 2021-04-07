1004. Max Consecutive Ones III

when K >= 0, we only move j to expand the windown size, when K < 0, we move i along with j so the window size will not change

so if the subarray ending in i, the subarray has to be bigger than the biggest we have found, if not, it is not the answer

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(A):
            print(j,i, K)
            if A[i] == 0:
                K -= 1
        
            if K < 0:
                if A[j] == 0:
                    K += 1
                j = j+ 1

            i += 1
        
        return i - j

    
    
#     def longestOnes(self, A, K):
#         i = 0
#         for j in range(len(A)):
#             K -= 1 - A[j]
#             if K < 0:
#                 K += 1 - A[i]
#                 i += 1
#             j += 1
#         return j - i
    
    
a = Solution()
print(a.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

0 0 3
0 1 2
0 2 1
0 3 1
0 4 1
0 5 0
1 6 0
1 7 0
1 8 0
1 9 0
2 10 0
2 11 0
2 12 0
3 13 -1
4 14 -2
5 15 -2
6 16 -1
7 17 -1
8 18 -1
9 19
10

print(a.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1], 3))
0 0 3
0 1 2
0 2 1
0 3 1
0 4 1
0 5 0
1 6 0
1 7 0
1 8 0
1 9 0
2 10 0
2 11 0
2 12 0
3 13 -1
4 14 -2
5 15 -2
6 16 -1
7 17 -1
8 18 -1
9 19 -1
10 20 0
10 21
11