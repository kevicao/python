#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Catalan Number
https://www.geeksforgeeks.org/program-nth-catalan-number/

catalan = c(2n,n)/(n+1)
c(n,k) = n!/k!/(n_k)! 简化后是 o(n)复杂度


# In[3]:


#22 generate all possible valid parenthesis for n pair ()
n = 9
def generate(A = []):
    if len(A) == 2*n:
        if valid(A):
            ans.append("".join(A))
    else:
        A.append('(')
        generate(A)
        A.pop()
        A.append(')')
        generate(A)
        A.pop()

def valid(A):
    bal = 0
    for c in A:
        if c == '(': bal += 1
        else: bal -= 1
        if bal < 0: return False
    return bal == 0

ans = []
generate()
print(len(ans))
        


# In[12]:


# 96. Unique Binary Search Trees
# num of possibke bst is catalan number
# Total number of possible Binary Trees with n different keys (countBT(n)) = countBST(n) * n!

 https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/

# Python3 prgroam to contrcut all unique 
# BSTs for keys from 1 to n 

# Binary Tree Node 
""" A utility function to create a 
new BST node """
class newNode: 

	# Construct to create a newNode 
	def __init__(self, item): 
		self.key=item 
		self.left = None
		self.right = None

# A utility function to do preorder 
# traversal of BST 
def preorder(root) : 

	if (root != None) : 
	
		print(root.key, end = " " ) 
		preorder(root.left) 
		preorder(root.right) 
	
# function for constructing trees 
def constructTrees(start, end): 

	list = [] 

	""" if start > end then subtree will be 
		empty so returning None in the list """
	if (start > end) : 
	
		list.append(None) 
		return list
	
	""" iterating through all values from 
		start to end for constructing 
		left and right subtree recursively """
	for i in range(start, end + 1): 
	
		""" constructing left subtree """
		leftSubtree = constructTrees(start, i - 1) 

		""" constructing right subtree """
		rightSubtree = constructTrees(i + 1, end) 

		""" now looping through all left and 
			right subtrees and connecting 
			them to ith root below """
		for j in range(len(leftSubtree)) : 
			left = leftSubtree[j] 
			for k in range(len(rightSubtree)): 
				right = rightSubtree[k] 
				node = newNode(i) # making value i as root 
				node.left = left # connect left subtree 
				node.right = right # connect right subtree 
				list.append(node) # add this tree to list 
	return list

# Driver Code 
if __name__ == '__main__': 

	# Construct all possible BSTs 
	totalTreesFrom1toN = constructTrees(1, 9) 

	""" Printing preorder traversal of 
		all constructed BSTs """
	print("Preorder traversals of all", 
				"constructed BSTs are") 
# 	for i in range(len(totalTreesFrom1toN)): 
# 		preorder(totalTreesFrom1toN[i]) 
	print(len(totalTreesFrom1toN)) 


# In[ ]:




