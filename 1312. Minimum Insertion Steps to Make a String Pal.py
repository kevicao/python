# 1312. Minimum Insertion Steps to Make a String Palindrome

# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/

# time limited exceed

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Base Cases

        if len(s) <= 1:
            return 0
        if len(s) == 2:
            return 0 if(s[0] == s[1]) else 1

        # Check if the first and last characters are
        # same. On the basis of the comparison result,
        # decide which subrpoblem(s) to call

        if(s[0] == s[-1]):
            return self.minInsertions(s[1:-1])
        else:
            return (min(self.minInsertions(s[:-1]),
                        self.minInsertions(s[1:])) + 1)


# dp to use memory
class Solution(object):
    def minInsertions(self, str1):
        """
        :type s: str
        :rtype: int
        """

        # Create a table of size n*n. table[i][j]
        # will store minimum number of insertions
        # needed to convert str1[i..j] to a palindrome.
        n = len(str1)
        
        table = [[0 for i in range(n)]
                    for i in range(n)]
        

        # Fill the table
        for gap in range(1, n):
            for l in range(n-gap):
                h = l + gap

                if str1[l] == str1[h]:
                    table[l][h] = table[l + 1][h - 1]
                else:
                    table[l][h] = (min(table[l][h - 1],
                                       table[l + 1][h]) + 1)

        # Return minimum number of insertions
        # for str1[0..n-1]
        return table[0][n - 1];