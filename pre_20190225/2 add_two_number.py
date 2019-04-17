# add two non-negative integer number represented as Linked list in reverse order

List1 = [2,4,3]
List2 = [5,6,4]  # 342 + 465 = 807

def add_two_number(List1, List2):
    result = []
    
    if len(List1) > len(List2):
        Short = List2
        Long = List1
    else:
        Short = List1
        Long = List2

    carry = 0        
    for index, x in enumerate(Short):
        result.append((Short[index] + Long[index])%10 + carry)
        carry = (Short[index] + Long[index])/10
        print carry
    
    if len(List1) != len(List2):   
        result.append(Long[index+1] + carry)
        result.append(Long[index+2:])
        
    print result
    
    return result
        
add_two_number(List1, List2)