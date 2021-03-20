103. Binary Tree Zigzag Level Order Traversal


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []        
        queue = [root]
        
        flag = True
        while len(queue) > 0:
            if flag:
                res.append([x.val for x in queue])
            else:
                queue.reverse()
                res.append([x.val for x in queue])
                queue.reverse()
                
            tmp = []
            for x in queue:
                if x.left:
                    tmp.append(x.left)
                if x.right:
                    tmp.append(x.right)
            queue = tmp
            flag = not flag       
        return res
            