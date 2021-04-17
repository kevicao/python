1381. Design a Stack With Increment Operation


# Design a stack which supports the following operations.

# Implement the CustomStack class:

# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
# void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
# int pop() Pops and returns the top of stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.



class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.size + 1 <= self.maxSize:
            self.stack.append(x)
            self.size += 1
        
        

    def pop(self):
        """
        :rtype: int
        """
        if self.size >= 1:
            self.size -= 1
            return self.stack.pop(-1)
            
        else:
            return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(0, min(k, self.size)):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)