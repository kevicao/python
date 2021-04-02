Sort by start and go through the list to merge


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])
        
        current = intervals[0]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] <= current[1]:
                if intervals[i][1] > current[1]:
                    current[1] = intervals[i][1]
            else:
                res.append(current)
                current = intervals[i]
        res.append(current)
        
        return res