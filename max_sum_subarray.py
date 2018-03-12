'''
find the continous subarray with max sum
https://en.wikipedia.org/wiki/Maximum_subarray_problem
'''

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    
    
def max_subarray_non(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print max_subarray(A) #6 [4, -1. 2, 1]

print max_subarray_non(A)
