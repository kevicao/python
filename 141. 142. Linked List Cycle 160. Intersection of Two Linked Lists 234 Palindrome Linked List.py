#!/usr/bin/env python
# coding: utf-8

# In[16]:



class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None


def llc(node):
    flag = -1
    if node.next is None:
        flag = False
    
    pointer1 = node.next
    pointer2 = node.next.next
    while pointer2 is not None:
#         print(pointer1.data, pointer2.data)
        if pointer1 == pointer2: 
            flag = True

            pointer1 = head
            while pointer1 != pointer2:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
                
            break

            
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
               
    return (flag, pointer1.data)

head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = head.next

# head = Node(1)
# head.next = Node(2)
# head.next.next = head

# head = Node(1)
# head.next = Node(2)

llc(head)


# 因为快指针每次走2，慢指针每次走1，快指针走的距离是慢指针的两倍。而快指针又比慢指针多走了一圈。所以head到环的起点+环的起点到他们相遇的点的距离 与 环一圈的距离相等。现在重新开始，head运行到环起点 和 相遇点到环起点 的距离也是相等的，相当于他们同时减掉了 环的起点到他们相遇的点的距离

# In[ ]:


#234 Given a singly linked list, determine if it is a palindrome
# find middle node using two pointer traveling at speed 1 and 2
# reverse second half and see if equal to first half

https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/

