#!/usr/bin/env python
# coding: utf-8

# In[25]:


#https://medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237
# HashMap will hold the keys and address of the Nodes of Doubly LinkedList . 
#And Doubly LinkedList will hold the values of keys.

class Node: 
    def __init__(self, key, data): 
        self.value = data 
        self.key = key
        self.next = None
        self.previous = None
        
class LRU:
    def __init__(self, size): 
        self.hash = dict()
        self.limit = size
        self.head = Node(None, None)  #most recetnly used
        self.end = Node(None, None) #least used
        self.head.next = self.end
        self.end.previous = self.head
        
    def get(self, key):
        if key in self.hash:
            #update linked list
            
            if self.end != self.hash[key]:
                self.hash[key].next.previous = self.hash[key].previous
                self.hash[key].previous.next = self.hash[key].next
            else:
                self.end = self.end.previous
                self.hash[key].previous.next = None
                
            if self.hash[key].next == self.end:
                self.end = self.end.previous
            
            
            self.hash[key].next = self.head
            self.head.previous = self.hash[key]
            self.head = self.hash[key]
            
            return self.hash[key].value
            
        else:
            return -1
        
    def put(self, key, value):
        if key in self.hash: # possbile different value
            self.hash[key].value = value
            #update linked list
            self.hash[key].next.previous = self.hash[key].previous
            self.hash[key].previous.next = self.hash[key].next
            
            self.hash[key].next = self.head
            self.head.previous = self.hash[key]
            self.head = self.hash[key]
            
            
        else: 
            if len(self.hash) == self.limit:
                #delete from hash
                print('should delete', self.end.key)
                self.hash.pop(self.end.key)
                
                #move tail first
                self.end.previous.next = None
                self.end = self.end.previous
                
            self.hash[key] = Node(key, value)
            
            if len(self.hash) == 1:
                self.head = self.hash[key]
                self.end = self.hash[key]
                self.head.next = self.end
                self.end.previous = self.head
                
            else:    
                self.hash[key].next = self.head
                self.head.previous = self.hash[key]
                self.head = self.hash[key]
                
                
cache = LRU(2)
cache.put(1, 1)
print(cache.head.key, cache.end.key, cache.hash)
cache.put(2, 2)
print(cache.head.key, cache.end.key, cache.hash)
print(cache.get(1))      # returns 1
print(cache.head.key, cache.end.key, cache.hash)
cache.put(3, 3);    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.head.key, cache.end.key, cache.hash)
print(cache.get(3))       # returns 3
print(cache.get(4))      # returns 4
        


# In[ ]:





# In[ ]:




