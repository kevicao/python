#!/usr/bin/env python
# coding: utf-8

# In[ ]:https://www.google.com/amp/s/www.geeksforgeeks.org/print-right-view-binary-tree-2/amp/


# we can store the value of the first node that we visit at each depth in DFS where we visit right first always
def rightSideView(root):
    rightmost_value_at_depth = dict() # depth -> node.val
    max_depth = -1

    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()

        if node is not None:
            # maintain knowledge of the number of levels in the tree.
            max_depth = max(max_depth, depth)

            # only insert into dict if depth is not already present.
            rightmost_value_at_depth.setdefault(depth, node.val)  #same with get, but will set default value if no key

            stack.append((node.left, depth+1))
            stack.append((node.right, depth+1))

    return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]

