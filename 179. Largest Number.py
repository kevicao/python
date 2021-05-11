179. Largest Number


https://leetcode.com/problems/largest-number/solution/

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
        
        
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x