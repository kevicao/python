169 229: Majority Element I and II



https://baihuqian.github.io/2018-07-10-majority-element-ii/

Use modified Boyer-Moore algorithm. There are at most two majority elements, and the number of non-majority elements must be fewer than either of them. Thus, we can maintain two counters. If a number equals to one of the candidates, the corresponding counter +1 while the other does not change; if a number does not equal to either of them, both counters -1. If a counter is 0, replace the candidate with the next number. At the end, verify both of them occurred more than ⌊ n/3 ⌋ times, because some times there is only one majority element.


# 169. Majority Element
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# and we can assume there is 1


# https://leetcode.com/problems/majority-element/solution/
# this actually explian why it works (last solution)

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate