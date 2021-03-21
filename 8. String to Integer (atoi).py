8. String to Integer (atoi)


many special cases is not mentioned in the problem description
+/-/space has to be before any digit
space has to be before everything

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sign = 1
        res = ''
        flag = 0
        count = 0
        while i < len(s):
            if count == 0 and flag == 0 and s[i] == ' ':
                i += 1
            elif count == 0 and flag == 0 and s[i] in ('-'):
                sign = -1
                i += 1
                flag = 1
            elif count == 0 and flag == 0 and s[i] == '+':
                sign = 1
                i += 1
                flag = 1
            elif (s[i]).isdigit():
                count += 1
                res += s[i]
                i += 1
            else:
                break
                
        if len(res) > 0:
            if sign == 1:
                return min(sign*int(res), 2**31-1)
            elif sign == -1:
                return max(sign*int(res), -2**31)
        else:
            return 0
