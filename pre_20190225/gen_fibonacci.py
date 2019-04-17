
"""
#fibonacci numbers
#generate the nth fibonacci number [0,1,1,2,3,5,8,.......]

@author: Jianghui
"""

def gen_fibonacci(n):
    ''' recursive calls, complexitiy is 2^n '''
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    return gen_fibonacci(n-1) + gen_fibonacci(n-2)
    
    
def gen_fibonacci_dp(fib, i):
    ''' complexity n'''
    if i == 0:
        return 0
        
    if fib[i] != 0:
        return fib[i]
    else:
        index = i
        while fib[index] == 0:
            index -= 1
        for j in range(index+1, i+1):
            fib[j] = fib[j-1] + fib[j-2] #save results
            
    return fib[i]
    
fib = [0]*50
fib[0] = 0
fib[1] = 1

print gen_fibonacci_dp(fib, 10)
print fib