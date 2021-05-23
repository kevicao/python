605. Can Place Flowers
facebook number of 0 that can be turned into 1

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        
        if len(flowerbed) == 0:
            return 0 >= n
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 >= n
            else:
                return 0 >= n
        
        for i in range(len(flowerbed)):
        	# if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0))
            if flowerbed[i] == 0:
                if (i == 0 and flowerbed[i+1] == 0) or (i == len(flowerbed)  - 1 and flowerbed[i-1] == 0) or (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    count += 1
            
        return count >= n
        