1460. Make Two Arrays Equal by Reversing Sub-arrays

# order does not matter, actually check whehte having same number of unqiue numbers
class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        h = {}
        for x in target:
            if x in h:
                h[x] += 1
            else:
                h[x] = 1
        
        for x in arr:
            if x not in h:
                return False
            else:
                h[x] -= 1
                if h[x] == 0:
                    del h[x]
                
            
        return True

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target_sorted = sorted(target)
        arr_sorted = sorted(arr)
        for i in range(len(target)):
            if target_sorted[i] != arr_sorted[i]:
                return False
        else:
            return True 


class Solution(object):
    def canBeEqual(self, array_a, array_b):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(array_a):
            if array_a[i] == array_b[i]:
                i += 1
            else:
                j = i + 1
                flag = False
                while j < len(array_a):
                    if array_a[i] == array_b[j]:
                        flag = True
                        for k in range(0,(j-i)//2+1):
                            array_b[i+k], array_b[j-k] = array_b[j-k], array_b[i+k]
                        break
                    else:
                        j += 1
                if not flag:
                    return False
                else:
                    i += 1
        return True      