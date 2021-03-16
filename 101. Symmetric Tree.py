#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isSymmetric(root): 
    return isMirror(root, root)


def isMirror(t1, t2):
    if t1 == null and t2 == null:
        return True
    
    if t1 == null or t2 == null: 
        return False;
    
    return (t1.val == t2.val)        and isMirror(t1.right, t2.left)        and isMirror(t1.left, t2.right)

isSymmetric([1,2,2,3,4,4,3])    


# In[11]:


def isSymmetric(tree, root):
    return isMirror(tree, root, root)


def isMirror(tree, r1, r2):
    print(r1, r2)
    if (r1 >= len(tree) and r2 >= len(tree)) or (tree[r1] is None  and tree[r2] is None):
        return True
    
    if tree[r1] is None or tree[r2] is None or r1 >= len(tree) or r2 >= len(tree): 
        return False
    
    return (tree[r1] == tree[r1])        and isMirror(tree, r1*2+2, r2*2+1)        and isMirror(tree, r1*2+1, r2*2+2)

isSymmetric([1,2,2,3,4,4,3],0)  #true
# isSymmetric([1,2,2,None,3,None,3], 0)


# In[1]:


a = None
if a:
    print('here')


# In[ ]:




