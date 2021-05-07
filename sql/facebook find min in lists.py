# k lists
# each list is sorted, up to n inegers

# arr = [[], [1,2]]

class find_next_minimum(object):
    def __init__(self, arr):
        #deal with empty
        import heapq 
        self.arr = arr
        #each tuple (value, index_element, index_list)
        
        self.h = [(x[0], 0, i) for i,x  in enumerate(self.arr) if len(x) > 0]
        heapq.heapify(self.h)
        
    def hasNext(self):
        #how to find size of h
        if len(self.h) > 0:
            return True
        else:
            return False
        
    
    def Next(self):
        if self.hasNext():
            minimum, index_element, index_list = heapq.heappop(self.h)

            if index_element < len(self.arr[index_list]) - 1:
                index_element += 1
                heapq.heappush(self.h, (self.arr[index_list][index_element], index_element, index_list))
                
            return minimum
        
        else:
            return 'no more'
    
    

    