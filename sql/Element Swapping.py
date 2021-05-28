# facebook interview pratice Element Swapping

# Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.
# Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.

def findMinArray(arr, k):
  # Write your code here
    l = 0
    
    while k >0:
        m = min(k, len(arr)-l-1 )
        index = find_min_index(arr[l+1:l+m+1])
        minimum = arr[l+index+1]
        if minimum < arr[l]:
            arr[l+1:l+index+2] = arr[l:l+index+1]
            arr[l] = minimum
            k -= (index+1)
            
    return arr
        
def find_min_index(arr):
    minimum = arr[0]
    index = 0
    for i in range(1,len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            index = i
    return index 

# the folowing use the same idea
# https://www.geeksforgeeks.org/lexicographically-smallest-array-k-consecutive-swaps/