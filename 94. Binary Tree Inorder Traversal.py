
#recursion
class Node:
    def __init__(self, value=0, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

C = Node(3, None, None)
B = Node(2, C, None)
A = Node(1, None, B)


def inorder_traversal(root):
    if root is None:
        return []
    elif root.left is None and root.right is None:
        return [root.value]    
    else:
        return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

inorder_traversal(A)



# array representation: p, 2p+1 for left, 2p+2 for right

L = [1, None, 2, None, None, 3]

def inorder_recur(L, root):
    if root >= len(L) or L[root] == None:
        return []
    elif root*2+1 < len(L) and L[root*2+1] is None            and root*2+2 < len(L) and L[root*2+2] is None:
        return [L[root]]
    else:
        return inorder_recur(L, root*2+1) + [L[root]] + inorder_recur(L, root*2+2)
    
inorder_recur(L, 0)


# itteration
# https://www.cnblogs.com/bymo/p/9591063.html
def inorder_iter(L):
    stack = []
    res = []
    
    root = 0
    while (root < len(L) and L[root]) or stack:
        print(stack)
        while root < len(L) and L[root]:
            print('here', stack)
            stack.append(root)
            print('there', stack)
            root = root*2 + 1
        
        tmp = stack.pop()
        res.append(L[tmp])
        root = tmp*2 + 2
        
    return res

L = [1, None, 2, None, None, 3]
# inorder_iter(L) #1,3,2
L = [1, 2, 3, 4, 5]
inorder_iter(L)  #4,2,5,1,3


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

D = Node(4, None, None)
E = Node(5, None, None)
B = Node(2, D, E)
C = Node(3)
A = Node(1, B, C)

class Solution(object):       
    def inorderTraversal(self, root):  # 迭代
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def preorderTraversal(self, root):  # 迭代
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    def postorderTraversal(self, root):  # 迭代
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            while root:
                if root.right: 
                    stack.append(root.right) 
                stack.append(root)

                root = root.left        
            root = stack.pop()
            if root.right and (len(stack) > 0 and stack[-1] == root.right): 
                stack.pop() # Remove right child from stack 
                stack.append(root) # Push root back to stack 
                root = root.right # change root so that the 
                                # right childis processed next 

            else: 
                res.append(root.val) 
                root = None

        return res
        
s = Solution()
# s.inorderTraversal(A)
# s.preorderTraversal(A)
s.postorderTraversal(A)