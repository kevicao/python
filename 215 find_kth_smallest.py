
# Given an integer array nums and an integer k, return the kth largest element in the array.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, k)
    
    def quickSelect(self, nums, start, end, k):
        while True:
            #ri = randint(start, end)   this random selection is completly optional, but using this will improve the speed of the program
            #self.swap(nums, ri, start)
            pivot, left, right = start, start + 1, end
            while left <= right:
                if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                    self.swap(nums, left, right)
                if nums[left] <= nums[pivot]:
                    left += 1
                if nums[right] >= nums[pivot]:
                    right -= 1
            
            self.swap(nums, pivot, right)
            if k == right:
                return nums[right]
            elif k < right:
                end = right - 1
            else:
                start = right + 1
                
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]



#########too much space

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        array = nums
        pivot = 0
        left = []
        right = []
        # right_index = len(n) - 1 for in place swap

        print(array, k)

        for i in range(1,len(array)):
            if array[i] >= array[pivot]:
                # use too much extra space, can be done in original array
                # swap pivot element and i element in the array
                left.append(array[i])
            else:
                right.append(array[i])


        if len(left) == k-1:  ##pivot is median
            return array[pivot]
            
        elif len(left) >= k: 
            return self.findKthLargest(left, k)
            
        else:
            print(right, k, len(left))
            return self.findKthLargest(right, k-len(left)-1)






'''
find the kth smallest number in two sorted array
https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
'''
def kth(arr1, arr2, m, n, k):
 
    sorted1 = [0] * (m + n)
    i = 0
    j = 0
    d = 0
    while (i < m and j < n):
 
        if (arr1[i] < arr2[j]):
            sorted1[d] = arr1[i]
            i += 1
        else:
            sorted1[d] = arr2[j]
            j += 1
        d += 1
 
    while (i < m):
        sorted1[d] = arr1[i]
        d += 1
        i += 1
    while (j < n):
        sorted1[d] = arr2[j]
        d += 1
        j += 1
    return sorted1[k - 1]
        
A = [10, 20, 40, 60]
B = [15, 35, 50, 70, 100]

print find_kth_smallest(A, B, 4) # 35