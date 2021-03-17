1288. Remove Covered Intervals

remove intervals covered by another one and return the number of remaining intervals



class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        
        i = 0
        res = []
        while i < len(intervals):
            j = i+1
            
            while j < len(intervals) and intervals[j][1] <= intervals[i][1]:
                
                j += 1
                
            res.append(intervals[i])
            i = j
            
        return len(res)