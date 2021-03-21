# 391. Perfect Rectangle

# all rectangles form a bigger one without blank space, no overlap


# the large rectangle area should be equal to the sum of small rectangles
# count of all the points should be even, and that of all the four corner points should be one

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        if len(rectangles) == 0 or len(rectangles[0]) == 0:
            return False
        
        x1 = float('inf')
        x2 = float('-inf')
        y1 = float('inf')
        y2 = float('-inf')
        
        s = dict()
        area = 0
        
        for rec in rectangles:
            x1 = min(rec[0], x1)
            y1 = min(rec[1], y1)
            x2 = max(rec[2], x2)
            y2 = max(rec[3], y2)
            
            area += (rec[2] - rec[0])*(rec[3] - rec[1])
            
            temp = dict()
            temp[1] = str(rec[0]) + ' ' + str(rec[1])
            temp[2] = str(rec[0]) + ' ' + str(rec[3])
            temp[3] = str(rec[2]) + ' ' + str(rec[3])
            temp[4] = str(rec[2]) + ' ' + str(rec[1])
            
            for x in range(1,5):
                if temp[x] in s:
                    del s[temp[x]]
                else:
                    s[temp[x]] = 1
            

        if (str(x1) + ' ' + str(y1) not in s) or (str(x1) + ' ' + str(y2) not in s) or (str(x2) + ' ' + str(y1) not in s) or (str(x2) + ' ' + str(y2) not in s) or len(s) != 4:
            return False

        return area == (x2-x1)*(y2-y1)
                
            



# we can also determine overlap or not first 
# (can follow 1288 to remove covered intervals by sort by x1, -x2, whose time complexity is N*log(N))
# , then sum ( each area) = max possible area

# This does not meet time limie


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        #no overalp
        rectangles = sorted(rectangles, key = lambda x: (x[0], -x[3]))
        
        i = 0
        for i in range(len(rectangles)):
            j = i+1
            while j < len(rectangles) and rectangles[j][0] < rectangles[i][2]:
                if rectangles[j][1] < rectangles[i][3] and rectangles[j][1] >= rectangles[i][1]:
                    return False
                elif rectangles[j][3] <= rectangles[i][3] and rectangles[j][3] > rectangles[i][1]:
                    return False
                else:
                    j += 1
            i = j
                        
        
        xmin = min([x[0] for x in rectangles])
        xmax = max([x[2] for x in rectangles])
        ymin = min([x[1] for x in rectangles])
        ymax = max([x[3] for x in rectangles])
        
        areas = [(x[2] - x[0])*(x[3]-x[1]) for x in rectangles]
        
        print(areas)
        print((xmax - xmin)*(ymax - ymin))
        return (xmax - xmin)*(ymax - ymin) == sum(areas)



# we can use the solution from 850: rectangle area II, whose time complexity is N^3
# if sum(each area) = rectangle area II == (max(x) - min(x))*(maxy - miny)

# does not meet time limit

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        xmin = min([x[0] for x in rectangles])
        xmax = max([x[2] for x in rectangles])
        ymin = min([x[1] for x in rectangles])
        ymax = max([x[3] for x in rectangles])
        
        areas = [(x[2] - x[0])*(x[3]-x[1]) for x in rectangles]
        
        print(areas)
        print((xmax - xmin)*(ymax - ymin))
        return (xmax - xmin)*(ymax - ymin) == sum(areas) == self.rectangleArea(rectangles)
        
        
    def rectangleArea(self, rectangles):
        N = len(rectangles)
        Xvals, Yvals = set(), set()
        for x1, y1, x2, y2 in rectangles:
            Xvals.add(x1); Xvals.add(x2)
            Yvals.add(y1); Yvals.add(y2)

        imapx = sorted(Xvals)
        imapy = sorted(Yvals)
        mapx = {x: i for i, x in enumerate(imapx)}
        mapy = {y: i for i, y in enumerate(imapy)}

        grid = [[0] * len(imapy) for _ in imapx]
        for x1, y1, x2, y2 in rectangles:
            for x in xrange(mapx[x1], mapx[x2]):
                for y in xrange(mapy[y1], mapy[y2]):
                    grid[x][y] = 1

        ans = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val:
                    ans += (imapx[x+1] - imapx[x]) * (imapy[y+1] - imapy[y])
        return ans