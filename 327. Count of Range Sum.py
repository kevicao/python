327. Count of Range Sum



class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        subsums = [0]*(len(nums)+1) #record every sub sum from the first element to ith 
        index = 1 #subsum at 0 is 0, as we start from 1
        for i in nums:
            subsums[index] = subsums[index-1] + i
            index += 1
        
        BIT = [0]*(len(subsums)+1) #build BIT to store the occurence of every sub sum
        # 0 node in BIT is the parent and not useful to store info
        
        def update(x):
            while x <= len(BIT)-1:
                BIT[x] += 1 #add one occurence for this subsum 
                x += (x&-x)
        
        def query(x):
            res = 0
            while x > 0:
                res += BIT[x] #add the occruence of this subsum
                x -= (x&-x) 
            return res
        
        sortedsubsums = sorted(subsums)
        final = 0
        for subsum in subsums:
            lo = query(bisect.bisect_right(sortedsubsums, subsum-lower)) #lo stands for the sum of the occurreces of subsums equal/higher than lower
            hi = query(bisect.bisect_left(sortedsubsums, subsum-upper))
            final += (lo - hi) #get all existing occurences of subsums that 
            update(bisect.bisect_right(sortedsubsums,subsum))
        return final 