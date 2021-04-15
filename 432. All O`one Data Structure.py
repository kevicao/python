432. All O`one Data Structure


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}
        self.min_key = ''
        self.max_key = ''

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key in self.h:
            self.h[key] += 1
        else:
            self.h[key] = 1
            
        if ((self.max_key in self.h) and (self.h[self.max_key] < self.h[key])) or (self.max_key == ''):
            self.max_key = key
        
        if self.min_key == key:
            count = float('inf')
            for key in self.h.keys():
                if self.h[key] < count:
                    self.min_key = key
                    count = self.h[key]           
            
        if ((self.min_key in self.h) and (self.h[self.min_key] > self.h[key])) or self.min_key == '':
            self.min_key = key
    

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if self.h[key] == 1:
            del self.h[key]
            if self.max_key == key:
                if self.h:
                    self.max_key = self.h.keys()[0]
                else:
                    self.max_key = ''
            if self.min_key == key:
                if self.h:
                    count = float('inf')
                    for key in self.h.keys():
                        if self.h[key] < count:
                            self.min_key = key
                            count = self.h[key]
                else:
                    self.min_key = ''
        else:
            self.h[key] -= 1
            if self.h[key] < self.h[self.min_key]:
                self.min_key = key
            if self.max_key == key:
                count = float('-inf')
                for key in self.h.keys():
                    if self.h[key] > count:
                        self.max_key = key
                        count = self.h[key]               
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.max_key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.min_key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()