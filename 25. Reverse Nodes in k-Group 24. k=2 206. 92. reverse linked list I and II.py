


def reverse(head):
  # Write your code here
# [x x |x x x| x x]
#    p  s   e  h
    dummy_head = Node(0)
    dummy_head.next = head
    prev = dummy_head
    running_prev = dummy_head
    s = None
    e = None
    
    flag = 0
    while flag <= 1:
        if head and (head.data%2 == 0):
            if not s:
                s = head
        else:
            if not s:
                print('here')
                prev = head
            if s and (not e):
                e = running_prev
                #print(s.data, e.data, prev.data, head.data)
        
        if s and e:
            #reverse
            tmp_h = s
            p = s.next
            while p != head:  
                tmp = p
                p = p.next
                tmp.next = tmp_h
                tmp_h = tmp
                
                
            prev.next = tmp_h
            s.next = head
            prev = head
            s = None
            e = None
            
        
        if head:
          running_prev = head       
          head = head.next
        if not head:
          flag += 1
        
    return dummy_head.next

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
        



# 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """      
        if not head:
            return head
        
        p = head.next
        head.next = None
        
        while p:
            print(p.val)
            tmp = p.next
            p.next = head
            head = p
            p = tmp
                        
        return head




# 92. Reverse Linked List II

# dummy is critical in the case that left = 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if (not head.next) or left == right:
            return head
        
        count = 1        
        p = head
        dummy = ListNode(next = head)
        prev = dummy
        end = head
        
        while count <= right:
            if count < left - 1:
                p = p.next
                
            elif count == left - 1:
                prev = p
                p = p.next

            elif count == left:
                end = p
                th = p.next
                p.next = None
                prev.next = p
                p = th
                print(p.val, prev.val, end.val)
                    
                
            else:
                th = p.next
                p.next = prev.next
                prev.next = p
                p = th
                print(prev.val, end.val)
                if count == right:
                    end.next = p
            

            count += 1
            
        
                
        return dummy.next