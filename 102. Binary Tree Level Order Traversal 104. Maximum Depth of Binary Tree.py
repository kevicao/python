#!/usr/bin/env python
# coding: utf-8

# In[20]:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


#List solution
#pq store the index of node in next level, so process pq one by one and build next pq (tmp_l)
def level_trav(L):
    pq = [0]
    ress = []
    res = []
    
    tmp_l = []
    
    depth = 0

    while pq:
        depth += 1
        for i in range(len(pq)): 

            tmp = pq[i]
            res.append(L[tmp])

            if tmp*2 + 1 < len(L) and L[tmp*2+1] is not None:
                tmp_l.append(tmp*2 + 1)
            
            if tmp*2 + 2 < len(L) and L[tmp*2+2] is not None:
                tmp_l.append(tmp*2 + 2)
                
        ress.append(res)
        res = []
        pq = tmp_l[:]
        tmp_l = []
            
    return (ress, depth)
    
level_trav([3,9,20,None,None,15,7])


# In[ ]:





# In[ ]:




