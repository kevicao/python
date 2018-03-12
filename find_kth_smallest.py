'''
find the kth smallest number in two sorted array
http://articles.leetcode.com/find-k-th-smallest-element-in-union-of/
'''
def find_kth_smallest(A,B,k):
    m = len(A)
    n = len(B)
    i = int(float(m)/(m+n)*(k-1))
    j = k-1 -i
    
    Ai_1 = -float('inf') if i == 0 else A[i-1]
    Bj_1 = -float('inf') if j == 0 else B[j-1]
    Ai = float('inf') if i == m else A[i]
    Bj = float('inf') if j == n else B[j]
    
    if Bj_1 < Ai and Ai < Bj:
        return Ai
    elif Ai_1 < Bj and Bj < Ai:
        return Bj
        
    if Ai < Bj:
        return find_kth_smallest(A[i+1:], B[:j], k-i-1)
    else:
        return find_kth_smallest(A[:i], B[j+1:], k-j-1)
        
A = [10, 20, 40, 60]
B = [15, 35, 50, 70, 100]

print find_kth_smallest(A, B, 4) # 35