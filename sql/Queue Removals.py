# Facebook practice: Queue Removals
# You're given a list of n integers arr, which represent elements in a queue (in order from front to back). You're also given an integer x, and must perform x iterations of the following 3-step process:
# Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
# Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it
# For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue
# Compute a list of x integers output, the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration.

def findPositions(arr, x):
  # Write your code here
    q = []
    for i,x in enumerate(arr):
        q.append([x,i+1])
    
    ans = []
    for i in range(min(x, len(arr))):
        l = min(x, len(q))
        max_index = find_max_index([x[0] for x in q[:l]])
        ans.append(q[max_index][1])
        for j in range(l):
            if j != max_index:
                q.append([max(q[j][0]-1,0), q[j][1]])
        q = q[l:]
        
    return ans
        
def find_max_index(arr):
    index = 0
    maximum = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
            index = i
    return index  



 #in place solution
 
def findPositions(arr, x):
  # Write your code here
    x = min(x, len(arr))
    
    result = []
    start = 0
    
    for i in range(x):
        readCount = min(x, len(arr) - i)
        
        maxPos = start
        maximum = arr[maxPos]
        while readCount > 0:
            if arr[start] != -1 :
                if maximum < arr[start]:
                    maximum = arr[start]
                    maxPos = start

                if (arr[start] > 0):
                    arr[start] = arr[start] - 1
                    
                readCount -= 1
            
            start += 1
            start = start % len(arr)
        
        arr[maxPos] = -1
        result.append(maxPos + 1)

    return result