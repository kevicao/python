# Given an sorted array containing n unique numbers taken from 0, 1, 2, ..., n,  find the one that is missing from the array

# Example:  
# input: [0,1,2,3,4,6]
# output: 5

# paypal

def find_missing(arr):
    L = 0
    R = len(arr)-1
    while L <= R:
        mid = (L + R)//2
        if arr[mid] == mid:
            L = mid + 1
        elif arr[mid] > mid and arr[mid-1] == mid -1:
            return mid
        else:
            R = mid - 1
            
Arr = [0,1,3,4,5,6]
find_missing(Arr)
