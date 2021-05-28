c#!/usr/bin/env python
# coding: utf-8

# #https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html
# 
# # O(n)
# 1. bucket sort: find biggerst value and make an array of that size. turn on index of element value
# 
# # O(n^2)
# 2. bubble sort: compare each adjecent number and swap if possible 
# 
# 3. selection sort: The algorithm works by selecting the smallest unsorted item and then swapping it with the item in the next position to be filled
# 
# 4. Insertion Sort: To sort unordered list of elements, we remove its entries one at a time and then insert each of them into a sorted part (initially empty):
# 
# # O(n log n)
# 
# 5. mergesort.  https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2868/
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        print(L)
        print(R)
        print('arr is', arr)
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
            
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
  

# 6. heapsort
# 
heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
        return [heappop(h) for i in range(len(h))]# 
# 7. quicksort: pick one (last or middle) and move smaller left and larger to right, repeat on both sides (divide and conquer (O(nlogn) or O(n^2)
# https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2870/
def partition(arr,low,high): 
    i = low-1
    pivot = arr[high]

    for j in range(low , high): 
        if arr[j] <= pivot: 
            # increment index of smaller element 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i+1 

def quickSort(arr,low,high): 
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 

        # Separately sort elements before 
        # partition position and after partition position
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 


# In[ ]:




