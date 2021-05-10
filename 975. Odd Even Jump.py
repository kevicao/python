975. Odd Even Jump

#same as the solution below but do better job at search

class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        K_ODD, K_EVEN = 0, 1
        
        n = len(arr)

        # Sorted nums list will contain all UNIQUE numbers (sorted ascending) from the arr list while
        # traversing arr in reverse.
        #
        # Nums idx is a dictionary which will store the lowest index for a number in arr.
        sorted_nums, nums_idx = [arr[-1]], {arr[-1]: n - 1}

        # DP list which at the end of the algorithm will store a boolean value whether it is possible to
        # reach the end of the list from a given index with either an odd or even jump.
        #
        # E. g.: [[True, False], [False, True], [True, True]]
        # index = 2: can reach the end of the list no matter the jump (since it is the end of the list)
        # index = 1: can reach the end of the list only if it is an EVEN jump
        # index = 0: can reach the end of the list only if it is an ODD jump
        dp = [[False, False] for _ in range(n)]
        dp[n - 1] = [True, True]

        # Traverse arr in reverse
        # Time: O(n)
        for i in range(n - 2, -1, -1):
            num = arr[i]
            sorted_n = len(sorted_nums)

            # Find the current number (its index) in the sorted nums list with binary search algorithm.
            # Time: O(logn)
            idx = bisect.bisect_left(sorted_nums, num)

            # If it is an odd jump, the above search result will point to a value higher or equal to
            # current number.
            if idx < sorted_n and sorted_nums[idx] >= num:
                dp[i][K_ODD] = dp[nums_idx[sorted_nums[idx]]][K_EVEN]

            # If it is an even jump, the above search result will point to a value that is equal to
            # current number OR decrease the index by one (if possible) to get the greatest number that
            # is lower than current number.
            if idx < sorted_n and sorted_nums[idx] == num:
                dp[i][K_EVEN] = dp[nums_idx[sorted_nums[idx]]][K_ODD]
            elif idx > 0:
                dp[i][K_EVEN] = dp[nums_idx[sorted_nums[idx - 1]]][K_ODD]

            # Add current number to the sorted nums list (only if not already in the list)
            # Time: O(n)
            if idx == sorted_n or sorted_nums[idx] != num:
                sorted_nums.insert(idx, num)

            # Assign the new index of current number
            nums_idx[num] = i

        # The result is the sum of True values for each index in the DP list for ODD jumps
        return sum(odd for odd, _ in dp)


# exceed time limit

class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        even = [0]*len(arr)
        even[-1] = 1
        odd = [0]*len(arr)
        odd[-1] = 1
        
        for i in range(len(arr)-2,-1,-1):
            #odd
            tmp = float('inf')
            tmp_index = -1
            for j in range(i+1, len(arr)):
                if arr[j] >= arr[i]:
                    if arr[j] < tmp:
                        tmp = arr[j]
                        tmp_index = j
            if tmp_index != -1 and even[tmp_index] == 1:
                odd[i] = 1
                
            #even
            tmp = -float('inf')
            tmp_index = -1
            for j in range(i+1, len(arr)):
                if arr[j] <= arr[i]:
                    if arr[j] > tmp:
                        tmp = arr[j]
                        tmp_index = j
            if tmp_index != -1 and odd[tmp_index] == 1:
                even[i] = 1                
            

        return sum(odd)