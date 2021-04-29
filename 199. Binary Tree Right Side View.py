199. Binary Tree Right Side View

#facebook problem: left view and return number of nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = [root]
        visible = []
        
        while queue:
            n = len(queue)
            visible.append(queue[-1].val)
            for i in range(n):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            queue = queue[n:]
            
        return visible
