2. Add Two Numbers


#add two numbers represented in reverse order as lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = (l1.val + l2.val)%10
        quote = (l1.val + l2.val)//10
        
        ans = ListNode(val)
        
        p1 = l1.next
        p2 = l2.next
        p3 = ans
        
        while p1 and p2:
            val = (p1.val + p2.val + quote)%10
            quote = (p1.val + p2.val + quote)//10
            
            p3.next = ListNode(val)
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next            
            
        while p1:
            val = (p1.val + quote)%10
            quote = (p1.val + quote)//10
            
            p3.next = ListNode(val)
            p3 = p3.next
            p1 = p1.next

        while p2:
            val = (p2.val + quote)%10
            quote = (p2.val + quote)//10
            
            p3.next = ListNode(val)
            p3 = p3.next
            p2 = p2.next
        
        if quote > 0:
            p3.next = ListNode(quote)
            
        return ans
