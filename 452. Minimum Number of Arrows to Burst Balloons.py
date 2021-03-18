452. Minimum Number of Arrows to Burst Balloons

# list of intervals
# for non-overlap, sort by second element
# for merging, sort by first element
# https://dev.to/rohithv07/452-minimum-number-of-arrows-to-burst-balloons-medium-17ec

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) == 0:
            return 0
         
        points = sorted(points, key=lambda x: x[1])
        
        count = 0
        end = float('-inf')
        
        for x in points:
            if x[0] > end:
                end = x[1]
                count += 1
                
                
        return count