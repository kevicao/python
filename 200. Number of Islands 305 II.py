#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np

def isl(data):
    isl_list = []
    counter = 2
    matrix = np.zeros((data.shape[0]+2, data.shape[1]+2))
    matrix[1:matrix.shape[0]-1,1:matrix.shape[1]-1] = data

    for i in range(1,matrix.shape[0]-1):
        for j in range(1,matrix.shape[1]-1):
            if matrix[i][j] == 1:
                if matrix[i-1][j] > 1:
                    matrix[i][j] = matrix[i-1][j]
                elif matrix[i+1][j] > 1:
                    matrix[i][j] = matrix[i+1][j]
                elif matrix[i][j-1] > 1:
                    matrix[i][j] = matrix[i][j-1]
                elif matrix[i][j+1] > 1:
                    matrix[i][j] = matrix[i][j+1]
                else:
                    matrix[i][j] = counter
                    counter += 1
    print(matrix)           
    return counter-2

matrix = np.array([[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]])
print(isl(matrix)) #1
matrix = np.array([[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]])
print(isl(matrix))
                    
            


# In[ ]:


#https://www.cnblogs.com/grandyang/p/4402656.html
#explain BFS and DFS


# In[ ]:


II

