'''
two element whose sum is cloest to 0
find/check pairs in unsorted array that gives sum = x
find paris with sum = 0
find pairs with sum cloest to 0
'''

def array_two_sum(A, sum):
    A.sort()
    
    l = 0
    r = len(A) - 1
    while l < r:
        if A[l] + A[r] == sum:
            return (True, A[l], A[r])
        elif A[l] + A[r] < sum:
            l += 1
        else:
            r -= 1
            
    return True
    
A = [1, 4, 45, 6, 10, -8, 12]
print array_two_sum(A, 16)

def array_two_sum_hash(A, SUM):
    hashmap = dict()
    
    for item in A:
        temp = SUM - item
        hashmap[item] = 1
        if temp in hashmap:
            print SUM, item, temp
            
    return
    
array_two_sum_hash(A, 16)
 HC
^][ C5\