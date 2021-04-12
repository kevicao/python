426. Convert Binary Search Tree to Sorted Doubly Linked List

# merge(fuse) two sorted linked lists
def concatenate_lists(head1, head2):
    
    if head1 == None:
        return head2

    if head2 == None:
        return head1
    
    # use left for previous.
    # use right for next.
    tail1 = head1.left
    tail2 = head2.left
    
    tail1.right = head2
    head2.left = tail1
    
    head1.left = tail2
    tail2.right = head1
    return head1

def convert_to_linked_list(root):
    
    if root == None:
        return None
    
    list1 = convert_to_linked_list(root.left)
    list2 = convert_to_linked_list(root.right)
    
    root.left = root.right = root
    result = concatenate_lists(list1, root)
    result = concatenate_lists(result, list2)
    
    return result



  #stack solution: https://www.cnblogs.com/Dylan-Java-NYC/p/11063883.html
  #not easy to understand