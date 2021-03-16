#!/usr/bin/env python
# coding: utf-8

# In[8]:


#http://bangbingsyb.blogspot.com/2014/11/leetcode-word-search.html
def exist(board, word):
    if len(board) == 0 or len(board[0]) == 0 :
        return false;
    
    visited = [[0]*len(board[0]) for x in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if findWord(board, visited, i, j, word, 0):
                return True;
        
    return False;


def findWord(board, visited, row, col, word, index):
    if index == len(word): 
        return True
    
    if row<0 or col<0 or row>=len(board)            or col>= len(board[0]) or visited[row][col] or board[row][col]!=word[index]: 
        return False;

    visited[row][col] = True;
    if findWord(board, visited, row-1, col, word, index+1): return True  
    if findWord(board, visited, row+1, col, word, index+1): return True
    if findWord(board, visited, row, col-1, word, index+1): return True
    if findWord(board, visited, row, col+1, word, index+1): return True
    visited[row][col] = False
    
    return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exist(board, 'ABCCED')
exist(board, 'ABFDAS')


# In[ ]:




