#!/usr/bin/env python
# coding: utf-8

# In[3]:https://www.google.com/amp/s/www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/amp/


# Python program to construct tree using inorder and 
# preorder traversals 

# A binary tree node 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

"""Recursive function to construct binary of size len from 
Inorder traversal in[] and Preorder traversal pre[]. Initial values 
of inStrt and inEnd should be 0 and len -1. The function doesn't 
do any error checking for cases where inorder and preorder 
do not form a tree """
def buildTree(inOrder, preOrder, inStrt, inEnd): 
	
	if (inStrt > inEnd): 
		return None

	# Pich current node from Preorder traversal using 
	# preIndex and increment preIndex 
	tNode = Node(preOrder[buildTree.preIndex]) 
	buildTree.preIndex += 1

	# If this node has no children then return 
	if inStrt == inEnd : 
		return tNode 

	# Else find the index of this node in Inorder traversal 
	inIndex = search(inOrder, inStrt, inEnd, tNode.data) 
	
	# Using index in Inorder Traversal, construct left 
	# and right subtrees 
	tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1) 
	tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd) 

	return tNode 

# UTILITY FUNCTIONS 
# Function to find index of vaue in arr[start...end] 
# The function assumes that value is rpesent in inOrder[] 

def search(arr, start, end, value): 
	for i in range(start, end + 1): 
		if arr[i] == value: 
			return i 

def printInorder(node): 
	if node is None: 
		return
	
	# first recur on left child 
	printInorder(node.left) 
	
	# then print the data of node 
	print(node.data) 

	# now recur on right child 
	printInorder(node.right) 
	
# Driver program to test above function 
inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 
# Static variable preIndex 
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1) 

# Let us test the build tree by priting Inorder traversal 
print("Inorder traversal of the constructed tree is")
printInorder(root) 


# In[ ]:

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_index = 0
        
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)  
 

a = Solution()
print(a.buildTree([3,9,20,15,7], [9,3,15,20,7]))



######################
nonlocal will not work in leetcode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    preorder_index = 0
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        
        def array_to_tree(left, right):
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)
            self.preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)