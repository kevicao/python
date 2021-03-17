# 560. Subarray Sum Equals K

# s1: two indexes to loop all possible pair, and calculate cummulatie sum in second loop

# s2: one loop to calculate cummulative sum; add the sum to map along with number of accurence. 
# The idea behind this approach is as follows: If the cumulative sum(represented by sum[i]sum[i] for sum up to i^{th}i 
# th
#   index) up to two indices is the same, the sum of the elements lying in between those indices is zero. Extending the same thought further, if the cumulative sum up to two indices, say ii and jj is at a difference of kk i.e. if sum[i] - sum[j] = ksum[i]−sum[j]=k, the sum of elements lying between indices ii and jj is kk.

# Based on these thoughts, we make use of a hashmap mapmap which is used to store the cumulative sum up to all the indices possible along with the number of times the same sum occurs. We store the data in the form: (sum_i, no. of occurrences of sum_i)(sum 
# i
# ​	
#  ,no.ofoccurrencesofsum 
# i
# ​	
#  ). We traverse over the array numsnums and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered, we also determine the number of times the sum sum-ksum−k has occurred already, since it will determine the number of times a subarray with sum kk has occurred up to the current index. We increment the countcount by the same amount.

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count
                    

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        map = {0:1}
        sum = 0
        for x in nums:
            sum += x
            if sum - k in map:
                count += map[sum - k]
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1

            
        return count
            
        
s = Solution()
s.subarraySum([1,1,1], 2)