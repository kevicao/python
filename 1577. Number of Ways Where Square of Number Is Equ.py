1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers

# Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

# Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
# Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.

class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return 0
        else:
            return self.Triplets(nums1, nums2) + self.Triplets(nums2, nums1)
    
    def Triplets(self, nums1, nums2):
        ans = 0
        for x in nums1:
            dic = defaultdict(int)
            sq = x**2
            for y in nums2:
                if sq%y == 0:
                    if sq//y in dic:
                        ans += dic[sq//y]
                    
                    if y in dic:
                        dic[y] += 1
                    else:
                        dic[y] = 1                   
        return ans
        

Position should not matter, count frequency and itterate
Unique value the same way

class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        cnt1 = collections.defaultdict(int)
        cnt2 = collections.defaultdict(int)
        for n in nums1:
            cnt1[n] += 1
        for n in nums2:
            cnt2[n] += 1

        def triplets(arr1, arr2):
            ans = 0
            for t, v in arr1.items():
                k = arr2.get(t, 0)
                tmp = k * (k - 1) // 2
                sq = t * t
                for m in arr2:
                    if m < t and sq % m == 0:
                        tmp += arr2.get(m, 0) * arr2.get(sq // m, 0)
                ans += tmp * v
            return ans
        return triplets(cnt1, cnt2) + triplets(cnt2, cnt1)
