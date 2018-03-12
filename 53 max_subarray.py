def max_subarray(A):
    max_ending_here = max_so_far = 0
    end = -1
    
    for index, x in enumerate(A):
        max_ending_here = max(0, max_ending_here + x)
        
        if max_ending_here >= max_so_far:
            max_so_far = max_ending_here
            end = index
        
    return (max_so_far, end)
    
    
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print max_subarray(A)

