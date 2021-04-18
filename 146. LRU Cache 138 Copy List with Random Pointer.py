#!/usr/bin/env python
# coding: utf-8

# In[25]:


#https://medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237
# HashMap will hold the keys and address of the Nodes of Doubly LinkedList . 
#And Doubly LinkedList will hold the values of keys.


# In[ ]: in this solution, head and tail is always dummy so we do not need check whehter node is tail or head


class Node: 
    def __init__(self, key, data): 
        self.value = data 
        self.key = key
        self.next = None
        self.previous = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.h = {}
        self.head = Node(None, None) #most used
        self.tail = Node(None, None) #least used
        self.head.next = self.tail
        self.tail.previous = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.h:
            self.h[key].previous.next = self.h[key].next
            self.h[key].next.previous = self.h[key].previous
            
            self.h[key].next = self.head.next
            self.head.next.previous = self.h[key]
            
            self.h[key].previous = self.head
            self.head.next = self.h[key]
            
            return self.h[key].value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.h:
            self.h[key].value = value
            
            self.h[key].previous.next = self.h[key].next
            self.h[key].next.previous = self.h[key].previous
            
            self.h[key].next = self.head.next
            self.head.next.previous = self.h[key]
            
            self.h[key].previous = self.head
            self.head.next = self.h[key]            
            
        else:
            if len(self.h) == self.capacity:
                #remove least used
                del self.h[self.tail.previous.key]
                
                self.tail.previous = self.tail.previous.previous
                self.tail.previous.next = self.tail
                
                
            self.h[key] = Node(key, value)
            
            self.h[key].next = self.head.next
            self.head.next.previous = self.h[key]
            
            self.h[key].previous = self.head
            self.head.next = self.h[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# In[ ]:




