25. Reverse Nodes in k-Group

# first check whether we have k left, if so, reverse the k nodes (when reverse, we work one by one, 
# and attach next one to front without connect las tone). once revese, we also need connect with before and after section
# https://medium.com/@jimdaosui/reverse-nodes-in-k-group-9d232e4a70a7

dummy
X,X,  X   |    X   ,X,    X     | X,X,X
    prev    prev2     nextPrev    cur
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (k == 1) or (not head) or (not head.next):
            return head
        
        dummy = ListNode(next = head)
        prev = dummy
    
        while True:
            count = 0
            current = prev.next
            while current:
                count += 1
                if current ==k:
                    break
                current = current.next
                
            if count < k:
                break
            
            nextPrev = prev.next
            
            prev2 = ListNode()
            cur = prev.next
            Next = ListNode()
            for i in range(k):
                Next = cur.next
                cur.next = prev2
                prev2 = cur
                cur = Next
                
            prev.next = prev2
            nextPrev.next = cur
            
            prev = nextPrev
                
        return dummy.next




# take k nodes and reverse, this pass time limit

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp_h = head
        h = [0]*k
        h[0] = head.next

        for i in range(1,k): 
            h[i] = h[i-1].next 
            
        for i in range(1,k):
            h[i-1].next = h[i].next
            h[i].next = temp_h.next
            temp_h.next = h[i]  
        
        temp_h = h[-1]
        
        while True:
            h[0] = h[k-1].next
            for i in range(1,k):
                if h[i-1].next: 
                    h[i] = h[i-1].next
                else:
                    break
            if i < k-1:
                break
            else:
                for i in range(1,k):
                    h[i-1].next = h[i].next
                    h[i].next = temp_h.next
                    temp_h.next = h[i]  
                temp_h = h[-1]
                
        return head
        
