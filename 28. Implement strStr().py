28. Implement strStr()


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        
        n = len(needle)
        
        for i, c in enumerate(haystack):
            if c == needle[0] and haystack[i:i+n] == needle:
                return i
            
        return -1