Count contiguous subarrays

# https://leetcode.com/discuss/interview-question/579606/count-contiguous-subarrays
def count_subarrays(arr):
#   Keep track of how many starting indexes we're carrying along for a ride    
    onboard = []
    
#     // Once we drop off the index from the stack we'll sum up the steps it traveled here.
    ways = [0]*len(arr)        
    
#     // Train's moving from L to R, picking up indices and carrying as max on left
    for i in range(0, len(arr)):      
#       // Drop off everyone that is too small
        while (onboard) and (arr[i] > arr[onboard[-1]]):
#         // dismounted is the index where this one started to travel with us.
            dismounted = onboard.pop()
    #         // Count how many steps this one travelled
            ways[dismounted] = i - dismounted  
#       // Pick up this index.
        onboard.append(i)
        print('onbaord',onboard)
    
#     // Drop off everyone that stayed on for the whole ride.
    while onboard:
        dismounted = onboard.pop()
        ways[dismounted] = len(arr) - dismounted
        
    print(ways)

    
#     // Train's moving from R to L, reverse of above... with max on right
    for i in range(len(arr) - 1, -1, -1):
#       // We'll always count one index as we did above, so don't double count it.
        ways[i] -= 1
      
#       // Drop off everyone that is too small
        while (onboard) and (arr[i] > arr[onboard[-1]]):
        #         // dismounted is the index where this one started to travel with us.
            dismounted = onboard.pop()
            #         // Count how many steps this one travelled
            ways[dismounted] += dismounted - i
      
        onboard.append(i)
    
#     // Drop off everyone that stayed on for the whole ride.
    while onboard:
        dismounted = onboard.pop();
        ways[dismounted] += dismounted + 1
        
    return ways


count_subarrays([3, 4, 1, 6, 2])


#clean comments
def count_subarrays(arr): 
    onboard = []
    ways = [0]*len(arr)        
    
    for i in range(0, len(arr)):      
        while (onboard) and (arr[i] > arr[onboard[-1]]):
            dismounted = onboard.pop()
            ways[dismounted] = i - dismounted  
        onboard.append(i)
    
    while onboard:
        dismounted = onboard.pop()
        ways[dismounted] = len(arr) - dismounted
        


    for i in range(len(arr) - 1, -1, -1):
        ways[i] -= 1
        while (onboard) and (arr[i] > arr[onboard[-1]]):
            dismounted = onboard.pop()
            ways[dismounted] += dismounted - i
      
        onboard.append(i)
    
    while onboard:
        dismounted = onboard.pop();
        ways[dismounted] += dismounted + 1
        
    return ways


count_subarrays([3, 4, 1, 6, 2])