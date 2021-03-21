218. The Skyline Problem

# sort all possible x values, and update each x's height 
# loop through x list to determine which to output

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        xvals = set()
        for b in buildings:
            xvals.add(b[0])
            xvals.add(b[1])
            
        xvals = sorted(xvals)
        
        xmap = {x:i for i,x in enumerate(xvals)}
        height = [0]*len(xvals)
        
        for b in buildings:
            for x in xvals[xmap[b[0]]:xmap[b[1]]]:
                height[xmap[x]] = max(height[xmap[x]], b[2])
         
        res = []
        i = 0
        while i < len(xvals):
            j = i+1
            while j< len(height) and height[j] == height[i]:
                j += 1

            res.append([xvals[i], height[i]])
            i = j
            j += 1
            
        return res