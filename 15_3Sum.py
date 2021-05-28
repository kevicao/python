Find all unique triplets in an array, giving sum of zero

#  find all a + b + c = 0 in an array of integers

# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# In[14]: loop from left to right to see if each can be included in one. The check could be 2sum or narrow down from both end in sorted array

# there could be duplicated elements; result can not have duplicates


class Solution(object):
    def threeSum(self, L):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        L = sorted(L)
        result = []

        for i in range(len(L)-2):
            l = i+1
            r = len(L)-1
            while l < r:
                if L[l] + L[r] + L[i] > 0:
                    r -= 1
                elif L[l] + L[r] + L[i] < 0:
                    l += 1
                else:
                    if [L[i], L[l], L[r]] not in result:
                        result.append([L[i], L[l], L[r]])
                    if L[l] == L[l+1]:
                        l += 1
                    elif L[r] == L[r-1]:
                        r -= 1
                    else:
                        l += 1
                        r -= 1

        return result
    


# In[15]:
#from leetcode discussion: faster, same logic

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [1]
        if len(nums)<3:
            return[]

        nums.sort()
        for i in range(0,len(nums)-2):
            if nums[i]>0:
                break
            if i>=1 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                #print(nums[left],nums[i],nums[right])
                if nums[left]+nums[i]+nums[right] == 0 and [nums[i],nums[left],nums[right]] != res[-1]:
                    res.append([nums[i],nums[left],nums[right]])
                    if nums[left]>nums[right]:
                        right-=1
                    else:
                        left+=1
                elif nums[left]+nums[i]+nums[right] > 0:
                    right -= 1
                else:
                    left+=1
        return res[1:]



# combine above two and the fatestclass Solution(object):
    def threeSum(self, L):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        L = sorted(L)
        result = [1]

        for i in range(len(L)-2):
            if L[i]>0:
                break
            if i>=1 and L[i] == L[i-1]:
                continue
                
            l = i+1
            r = len(L)-1
            while l < r:
                if L[l] + L[r] + L[i] > 0:
                    r -= 1
                elif L[l] + L[r] + L[i] < 0:
                    l += 1
                else:
                    if [L[i], L[l], L[r]] != result[-1]:
                        result.append([L[i], L[l], L[r]])
                    if L[l] == L[l+1]:
                        l += 1
                    elif L[r] == L[r-1]:
                        r -= 1
                    else:
                        l += 1
                        r -= 1

        return result[1:]



# leverge twoSum solution

def two_sum(List, target):
    Dict = dict()
    for index, x in enumerate(List):
        if x not in Dict.keys():
            Dict[target-x] = index
        else:
            print 'found the two number:', index, Dict[x]
            print List[index], List[Dict[x]]
            
            
def three_sum(List):
    solution = []
    for i in range(len(List)):
        
