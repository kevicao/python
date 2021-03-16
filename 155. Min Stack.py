#!/usr/bin/env python
# coding: utf-8

# In[5]:


#用另一个stack<int> trackMin来记录min值的变化，trackMin.top()表示当前最小值。
# 当有新的xi<=trackMin.top()被压入时，将xi压入trackMin变为新的当前最小值。
# 当xi==trackMin.top()时被pop出时，trackMin也同时pop。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []
        self.trackMin = []
        
    def push(self, x):
        if len(self.trackMin) == 0 or (len(self.trackMin) > 0 and x <= self.trackMin[-1]):
            self.trackMin.append(x)
            
        self.L.append(x)
        
        return None

    def pop(self):
        if len(self.L) == 0:
            return None
        
        if self.L[-1] == self.trackMin[-1]:
            self.trackMin.pop(-1)
            
        self.L.pop(-1)
        return None
        

    def top(self):
        if len(self.L) == 0:
            print('empty')
        else:
            return self.L[-1]
        

    def getMin(self):
        if len(self.L) == 0:
            print('empty')
        else:
            return self.trackMin[-1]

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())


# In[ ]:




