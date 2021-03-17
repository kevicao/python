138. Copy List with Random Pointer



# to copy a linked list, we can traverse and copy each node and insert it to the original list, we can then break it into two list
# we can assign random pointer after insert

# we can also travese and add orignal node and new node to a list and update accordingly

# https://www.programcreek.com/2012/12/leetcode-copy-list-with-random-pointer/



"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        # copy each node and insert to the list
        p = head
        while p:
            node = Node(p.val)
            node.next = p.next
            p.next = node
            p = node.next
            
        #copy random pointer
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
            
        #break the list into 2
        p = head
        newH = p.next
        while p:
            temp = p.next
            p.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            p = p.next
            
        return newH

        
# L = [[7,null],[13,0],[11,4],[10,2],[1,0]]


node0 = Node(1)
node1 = Node(10, next = node0)
node2 = Node(11, next = node1)
node3 = Node(13, next = node2)
node4 = Node(7, next = node3)

node0.random = node4
node1.random = node2
node2.random = node0
node3.random = node4


s = Solution()
# s.subarraySum([1,1,1], 2)

head = s.copyRandomList(node4)

# traverse the list
while True:
    print(head.val)
    if head.next:
        head = head.next
    else:
        break

