973. K Closest Points to Origin

Find K closest points to origin for a list of points on a plane

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda K: K[0]**2 + K[1]**2)

        return points[:k]   