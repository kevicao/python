460. LFU Cache



class Node():
    def __init__(self, k=None, v=None):
        self.k = k
        self.v = v  
        self.count = 0
        self.l = None
        self.r = None
        
    def __str__(self):
        return str(self.k)
    
class LFUCache:

    def __init__(self, capacity):
        self.node = {}  # key -> node
        self.first = {}  # use count -> first node in list, least latest used
        self.last = {}  # use count -> last node in list
        self.capacity = capacity   
        self.min_use_count = None
        
    # def Print(self):
    #     for k in sorted(self.first.keys()):
    #         print(f"{k}:", end=' ')
    #         n = self.first[k]
    #         while n:
    #             print((n.k,n.v,n.count), end=', ')
    #             n = n.r
    #         print()            
        
    def pop(self, node):
        if node.l and node.r:
            node.l.r, node.r.l = node.r, node.l
        elif node.l:
            # is last
            node.l.r = None
            self.last[node.count] = node.l
        elif node.r:
            # is first
            node.r.l = None
            self.first[node.count] = node.r
        else:
            # only elem
            self.first.pop(node.count, None)
            self.last.pop(node.count, None)
      
    def use(self, node):
        # -- update min use count
        if node.count == self.min_use_count and self.first[node.count] == self.last[node.count]:
            self.min_use_count +=  1
        # -- pop from current
        self.pop(node)        
        # -- insert to end of new
        node.count += 1
        node.r = None
        if node.count not in self.first:
            self.first[node.count] = node
        if node.count in self.last:   #need insert at last position, so we do not need do any in frist if the count is aleady there
            last = self.last[node.count]
            self.last[node.count], last.r, node.l = node, node, last
        else:
            self.last[node.count], node.l = node, None               
        
    def get(self, key):
        node = self.node.get(key, None)
        if node is None: 
            return -1        
        
        self.use(node)
        return node.v

    def put(self, key, value):
        
        # edge case
        if len(self.first)==0 and self.capacity==0:
            return
        
        # update case
        if key in self.node:
            node = self.node[key]
            node.v = value
            self.use(node)
            return
        
        # check capacity
        if self.capacity == 0:
            # remove least frequently used         
            n = self.first[self.min_use_count]   
            self.pop(n) 
            self.node.pop(n.k)
        
        # add
        node = Node(key, value)
        self.node[key] = node
        self.min_use_count = 1
        self.use(node)
        self.capacity = self.capacity-1 if self.capacity>0 else 0

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)