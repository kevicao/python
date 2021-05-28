543. Diameter of Binary Tree

Find largest distance between nodes in a tree

compare to largest sum 124: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        def preorder(node):
            if not node:
                return 0
            else:
                left = preorder(node.left)
                right = preorder(node.right)
                #at every node, check if it is the max diameter
                if left + right > self.diameter:  
                    self.diameter = left + right
                return 1 + max(left, right)
        
        preorder(root)
        return self.diameter   