1028. Recover a Tree From Preorder Traversal


# There are three cases for each depth. We keep current node and parent node, along with the current depth in the recursion.

# The depth is the same as the current level. In that case, just add the new node as the right child of the parent node. e.g. -1--2--3 where node 3 has to be added as the right child of node 1.
# The depth is 1 level deeper. In that case, add new node to the left child of the current node. e.g. -5--6 where node 6 has to be added as the left child of node 5.
# The depth is shallower. In that case, we use the level mapping to go back to the correct parent node, and add the new node as its right child. e.g. -10--20---30--40 where 
# the node 40 has a depth of 2 while node 30 has depth 3. The correct parent node should be node 10, since it has depth of 1.
# I am trying to be code as clean as possible - smaller functions are always preferred over long functions.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        def extract_D():
            j = 0
            while S[self.i + j] == '-':
                j += 1
            self.i += j
            return j

        def extract_num():
            num = 0
            while self.i < self.n and S[self.i].isdigit():
                num = 10*num + int(S[self.i])
                self.i += 1
            return num
    
        self.n = len(S)
        self.i = 0
        num = extract_num()
        self.root = TreeNode(num)
        self.levelmap = {0: self.root}
        
        def dfs(D, node, parent):
            if self.i == self.n:
                return None
            level = extract_D()
            num = extract_num()
            new = TreeNode(num)
            if level == D:
                parent.right = new
                self.levelmap[D] = new
                dfs(D, new, parent)
            elif level > D:
                node.left = new
                self.levelmap[D+1] = new
                dfs(D+1, new, node)
            else:
                parent = self.levelmap[level-1]
                parent.right = new
                self.levelmap[level] = new
                dfs(level, new, parent)

        dfs(0, self.root, None)
        return self.root

# Serialize / deserialize binary tree
# There can be multiple approaches to serialize and deserialize the tree. One approach is to perform a depth-first traversal and serialize individual nodes to the stream. We’ll use a pre-order traversal here. We’ll also serialize some markers to represent a null pointer to help deserialize the tree.

# Consider the below binary tree as an example. Markers (M*) have been added in this tree to represent null nodes. The number with each marker i.e. 1 in M1, 2 in M2, merely represents the relative position of a marker in the stream.

MARKER = '#'
def serialize(node, stream):
    if node == None:
        stream.dump(MARKER);
        return
    stream.dump(node.data);
    serialize(node.left, stream)
    serialize(node.right, stream)

def deserialize(stream):
    try:
        data = pickle.load(stream)
        if data == MARKER:
            return None

        node = BinaryTreeNode(data);
        node.left = deserialize(stream)
        node.right = deserialize(stream)
        return node
    except pickle.UnpicklingError:
        return None
    

