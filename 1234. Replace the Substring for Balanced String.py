1234. Replace the Substring for Balanced String

# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

# A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

# Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

# Return 0 if the string is already balanced.


class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        for key in ['Q', 'W', "E", 'R']:
            dic[key] = 0
            
        for i in range(len(s)):
            dic[s[i]] += 1

        
        print(dic)
        res = len(s)
        left = 0
        for right in range(len(s)):
            dic[s[right]] -= 1
            while left < len(s) and dic['Q'] <= len(s)/4 and dic['W'] <= len(s)/4 and dic['E'] <= len(s)/4 and dic['R'] <= len(s)/4:
                res = min(res, right - left + 1)
                print(left, right)
                dic[s[left]] += 1
                left += 1
            
        return res