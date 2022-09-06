class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n7 = TreeNode(7)
n15 = TreeNode(15)
n20 = TreeNode(20,n15,n7)
n9 = TreeNode(9)
n3 = TreeNode(3,n9,n20)

# bfs
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        res = [[root.val]]
        cur = [root]
        while cur:
            tmp = []
            tmp_node = []
            for x in cur:
                if x.left != None:
                    tmp.append(x.left.val)
                    tmp_node.append(x.left)
                if x.right != None:
                    tmp.append(x.right.val)
                    tmp_node.append(x.right)
            if tmp:
                res.append(tmp)
            cur = tmp_node
        
        return res

s = Solution()
s.levelOrder(n3)

# dfs
def printInorder(root):
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)
        
printInorder(n3)

def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
        
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val),
