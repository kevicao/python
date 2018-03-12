#rotated array
def search_rotated_array(A,a):
    start = 0
    end = len(A) - 1
    found = False
    index = -1
    
    while start <= end and not found:
        mid = (start + end)/2
        if A[mid] == a:
            found = True
            index = mid
            
        elif start == end and found == False:
            break
        else:
            if A[start] > A[mid - 1]:
                if a >= A[mid + 1] and a <= A[end]:
                    start = mid + 1
                else:
                    end = mid -1
            else:
                if a >= A[start] and a <= A[mid -1]:
                    end = mid -1
                else:
                    start = mid + 1
                    
    return index
    
A = [4,5,6,7,0,1,2]
A = [3,1,2]

print search_rotated_array(A,3)