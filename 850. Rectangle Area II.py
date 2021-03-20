850. Rectangle Area II



# Suppose instead of rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]], we had [[0,0,200,200],[100,0,200,300],[100,0,300,100]]. The answer would just be 100 times bigger.

# What about if rectangles = [[0,0,2,2],[1,0,2,3],[1,0,30002,1]] ? Only the blue region would have area 30000 instead of 1.

# Our idea is this: we'll take all the x and y coordinates, and re-map them to 0, 1, 2, ... etc. For example, if rectangles = [[0,0,200,200],[100,0,200,300],[100,0,300,100]], we could re-map it to [[0,0,2,2],[1,0,2,3],[1,0,3,1]]. Then, we can solve the problem with brute force. However, each region may actually represent some larger area, so we'll need to adjust for that at the end.

# Algorithm

# Re-map each x coordinate to 0, 1, 2, .... Independently, re-map all y coordinates too.

# We then have a problem that can be solved by brute force: for each rectangle with re-mapped coordinates (rx1, ry1, rx2, ry2), we can fill the grid grid[x][y] = True for rx1 <= x < rx2 and ry1 <= y < ry2.

# Afterwards, each grid[rx][ry] represents the area (imapx(rx+1) - imapx(rx)) * (imapy(ry+1) - imapy(ry)), where if x got remapped to rx, then imapx(rx) = x ("inverse-map-x of remapped-x equals x"), and similarly for imapy.



class Solution(object):
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
        return ans % (10**9 + 7)