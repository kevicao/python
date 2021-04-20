307. Range Sum Query - Mutable


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