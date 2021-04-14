380. Insert Delete GetRandom O(1)


# only insert when not present

class RandomizedSet(object):
    import random

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        else:
            self.arr.append(val)
            self.dic[val] = len(self.arr) - 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        else:
            self.dic[self.arr[-1]] = self.dic[val]
            self.arr[-1], self.arr[self.dic[val]] = self.arr[self.dic[val]], self.arr[-1]
            self.arr.pop(-1)
            del self.dic[val]
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.arr)
        

# 381. also insert if present

class RandomizedSet(object):
    import random

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        else:
            self.arr.append(val)
            self.dic[val] = len(self.arr) - 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        else:
            self.dic[self.arr[-1]] = self.dic[val]
            self.arr[-1], self.arr[self.dic[val]] = self.arr[self.dic[val]], self.arr[-1]
            self.arr.pop(-1)
            del self.dic[val]
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.arr)
        




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()