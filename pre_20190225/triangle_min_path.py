'''
triangle min path
http://www.programcreek.com/2013/01/leetcode-triangle-java/
'''

def triangle_min_path(A):
    total = [0]*len(A)
    
    for i in range(len(A)):
        total[i] = A[len(A)-1][i]
        
    for i in range(len(A)-2, -1, -1):
        for j in range(len(A[i])):
            total[j] = A[i][j] + min(total[j], total[j+1])
            
    return total
    
A = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
] 
#11 = 2 + 3 + 5 + 1

print triangle_min_path(A)

