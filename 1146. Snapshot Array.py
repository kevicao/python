1146. Snapshot Array

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.h = defaultdict(defaultdict) 
        self.n = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.h[self.n][index] = val
        

    def snap(self):
        """
        :rtype: int
        """
        self.n += 1
        return self.n - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """

        while snap_id >= 0:
            if index in self.h[snap_id]:
                return self.h[snap_id][index]
            snap_id -= 1
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

