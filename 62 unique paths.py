import numpy as np



def unique_paths(m, n):
    Matrix = np.zeros((m,n))
    Matrix[:, n-1] = 1
    Matrix[n-1, :] = 1
    print Matrix
    
    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            Matrix[i,j] = Matrix[i+1, j] + Matrix[i, j+1]
            
    return Matrix[0, 0]
    
    
    
print unique_paths(3,3)

