#!/usr/bin/env python
# coding: utf-8

# In[ ]:


array representation: p, 2p+1 for left, 2p+2 for right


# In[13]:


tree = dict()
tree['root'] = dict()
tree['root']['key'] = 1
tree['root']['left'] = None
tree['root']['right'] = 'ela'

tree['ela'] = dict()
tree['ela']['key'] = 2
tree['ela']['left'] = 'wle'
tree['ela']['right'] = None

tree['wle'] = dict()
tree['wle']['key'] = 3
tree['wle']['left'] = None
tree['wle']['right'] = None

def inorder_traversal(tree, root):
    if root is None:
        return []
    elif tree[root]['left'] is None and tree[root]['right'] is None:
        return [tree[root]['key']]    
    else:
        return inorder_traversal(tree, tree[root]['left']) + [tree[root]['key']] +                     inorder_traversal(tree, tree[root]['right'])

inorder_traversal(tree, 'root')


# In[21]:


def node(value, left, right):
    tmp = dict()
    tmp['value'] = value
    tmp['left'] = left
    tmp['right'] = right
    
    return tmp

C = node(3, None, None)
B = node(2, C, None)
A = node(1, None, B)


def inorder_traversal(tree):
    if tree is None:
        return []
    elif tree['left'] is None and tree['right'] is None:
        return [tree['value']]    
    else:
        return inorder_traversal(tree['left']) + [tree['value']] +                     inorder_traversal(tree['right'])

inorder_traversal(A)


# In[24]:


L = [1, None, 2, None, None, 3]

def inorder_recur(L, root):
    if root >= len(L) or L[root] == None:
        return []
    elif root*2+1 < len(L) and L[root*2+1] is None            and root*2+2 < len(L) and L[root*2+2] is None:
        return [L[root]]
    else:
        return inorder_recur(L, root*2+1) + [L[root]] + inorder_recur(L, root*2+2)
    
inorder_recur(L, 0)


# In[47]:


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


# In[35]:


a = [1,2,3]
b = []
c = a.pop()
c


# In[ ]:




