# 1597 - Build Binary Expression Tree From Infix Expression

# https://leetcode.ca/2020-04-14-1597-Build-Binary-Expression-Tree-From-Infix-Expression/


class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    def expTree(self, s):

        prio = {'(':1, '+':2, '-':2, '*':3, '/': 3}

        def combine(ops, stack):
            root = Node(ops.pop(-1))
    #         right first, then left
            root.right = stack.pop(-1)
            root.left = stack.pop(-1)

            stack.append(root)

        ops = []
        stack = []

        for i in range(len(s)):
            ch = s[i]
            if (ch == '('):
                ops.append(ch);
            elif ch.isdigit(): 
                stack.append(Node(ch))
            elif (ch == ')'):
                while (ops[-1] != '('):
                    combine(ops, stack)
    
                ops.pop(-1);
            else:
                while ( (len(ops) > 0) and (prio[ops[-1]] > prio[ch]) ): 
                    combine(ops, stack);

                ops.append(ch)

        while len(stack) > 1:
            combine(ops, stack);

        return stack[-1]


a = Solution()
print(a.expTree('3*4-2*5'))

