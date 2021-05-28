"""
Question 2: 

Given a collection of n two dimensional points and a number k, 
return the k closest points to (0,0) by Euclidean distance.

Euclidean Distance 'd' of (x,y) from (0,0) is d^2 = x^2 + y^2

For example give a set of points [(3,5), (9,7), (6,4)] and k = 2 
your function might return [(6,4), (3,5)]

"""
class heap(object):
    def __init__(self, )
    
    def push(self, val):
        # keep heap structure; log(size)
        
    def pop(self):
        # delte the largest one, log(size)

def find_k_points(arr, k):
    h = heap()
    
    for p in arr:
        dis = p[0]**2 + p[1]**2
        if len(h) < k:
            h.push((dis,p))
        else:
            if dis < h[0][0]:
                h.pop()
                h.push((dis,p))
                 
    result = []  
    while h:
        result.append(h.pop()[1])
        
    return result
            
        
               
        

































"""
Question 1: 

Create a function which takes two inputs: a sorted integer array and a target number N. 
This function should return the count of times the target appears in the array. 

Example: for nums [1, 2, 3, 7, 7, 7, 9, 9] and a target of 7, this would return 3 since 7 appears 3 times in the array. 
         If the target is 4, it would return 0.
"""
[1, 2, 3, 7, 7, 7, 9, 9]

binary_search(arr, k, True)
l = 0, r = 7 mid = 3 return 3

binary_search(arr, k, False)
l = 0, r = 7 mid = 3, update l = 4
mid = 5 return 5

5 - 3 + 1 = 3

def binary_search(arr, k, first = True):
    if len(arr) == 0:
        return -1
    
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = l + (r-l)//2
        
        if first:
            if arr[mid] == k:
                if arr[mid -1] == k:
                    r = mid - 1
                else:
                    return mid
        else:
            if arr[mid] == k:
                if arr[mid + 1] == k:
                    l = mid + 1
                else:
                    return mid
        
        if arr[mid] > k:
            r = mid - 1
        
        elif arr[mid] < k:
            l = mid + 1
            
    return -1

def findOccTimes(arr, k):
    fist = binary_search(arr, k, True)
    if  first == -1:
        return 0
    else:
        return binary_search(arr[first:], k, True) - first + 1


