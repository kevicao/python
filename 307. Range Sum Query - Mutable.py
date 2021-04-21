307. Range Sum Query - Mutable


# https://leetcode.com/problems/range-sum-query-mutable/solution/
# partition the range into blocks of size sqrt(n)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        import math
        self.nums = nums

        self.block_size = int(math.floor(math.sqrt(len(self.nums))))
        self.arr_size = int(math.ceil(len(self.nums)*1.0/self.block_size))
        print(self.arr_size)
        self.block = [0]*self.arr_size
        
        for i in range(len(self.nums)):
            self.block[i//self.block_size] += self.nums[i] 
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.block[index//self.block_size] = self.block[index//self.block_size] - self.nums[index] + val
        self.nums[index] = val    

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        s = 0
        start_block = left//self.block_size
        end_block = right//self.block_size
        
        if start_block == end_block:
            for i in range(left, right + 1):
                s += self.nums[i]
        else:
            for i in range(left, (start_block+1)*self.block_size):
                s += self.nums[i]
            for i in range(start_block+1, end_block):
                s += self.block[i]
            for i in range(end_block*self.block_size, right + 1):
                s += self.nums[i]
            
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# segmented tree solution with array implementation

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        if len(nums) > 0:
            self.n = len(nums)
            self.tree = [0]*2*self.n
            
            j = 0
            for i in range(self.n, self.n*2):
                self.tree[i] = nums[j]
                j += 1
                
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
                
        print(self.tree)

    def update(self, pos, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        pos += self.n
        self.tree[pos] = val
        
        while pos > 0:
            left = pos
            right = pos
            
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            
            # parent is updated after child is updated
            self.tree[pos / 2] = self.tree[left] + self.tree[right]
            pos /= 2


    def sumRange(self, l, r):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        # // get leaf with value 'l'
        l += self.n
        # // get leaf with value 'r'
        r += self.n
            
        s = 0
        while l <= r:
            if l % 2 == 1: 
               s += self.tree[l]
               l += 1
            
            if r % 2 == 0:
               s += self.tree[r];
               r -= 1
            
            l /= 2
            r /= 2
        
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)