'''
biggest histogram area
https://siddontang.gitbooks.io/leetcode-solution/content/array/largest_rectangle_in_histogram.html
'''

def max_histogram_area(h):
    s = [] #used as a stack
    h.append(0)
    
    max_sum = 0
    i = 0
    while i < len(h):
        if len(s) == 0 or h[i] > h[s[-1]]:
            s.append(i)
            i += 1
        else:
            tmp = s[-1]
            s.pop()
            max_sum = max(max_sum, h[tmp]*(i if len(s) == 0 else i-s[-1]-1 ))
            
    return max_sum
    
print max_histogram_area([2,1,5,6,2,3]) #10

print max_histogram_area([1,5,5,5,2,9,2,9,2]) #16

print max_histogram_area([10,20,30,40]) 

print max_histogram_area([1,2]) 


