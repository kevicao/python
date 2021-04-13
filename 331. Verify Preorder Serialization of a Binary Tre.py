331. Verify Preorder Serialization of a Binary Tree


# a binary tree T is full if
# each node is either a leaf or
# possesses exactly two child
# nodes.

# If full binary T has I internal nodes, the number of leaves is L = I + 1.
# https://courses.cs.vt.edu/~cs3114/Fall09/wmcquain/Notes/T03a.BinaryTreeTheorems.pdf

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        #keep trimming leaf: change (number, #, #) to #
        
        ans = []
        count = 0
        for x in preorder.split(','):
            ans.append(x)
            while len(ans) >= 3 and ans[-1] == '#' and ans[-2] == '#' and ans[-3] != '#':
                ans.pop(-1)
                ans.pop(-1)
                ans.pop(-1)
                ans.append('#')
                
        if len(ans) == 1 and ans[0] == '#':
            return True
        else:
            return False
            

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # count of # must be 1 more than count of non-#
        
        count = 0
        items = preorder.split(',')
        for i, item in enumerate(items):
            count += 1 if item != "#" else -1
            if count == -1 and i < len(items)-1:
                return False

        return count == -1        