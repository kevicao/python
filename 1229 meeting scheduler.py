1229 meeting scheduler 

find ealierst common slots with duration 8 from two avaliability inerval list
sort by start time for both

class Solution(object):
    def meetingScheduler(self, slots1, slots2, duration):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])

        while len(slots1) > 0 and len(slots2) > 0:
            print(slots1)
            print(slots2)
            if slots1[0][1] < slots2[0][0]:
                slots1.pop(0)
            elif slots1[0][0] > slots2[0][1]:
                slots2.pop(0)
            elif min(slots1[0][1], slots2[0][1]) - max(slots1[0][0], slots2[0][0]) >= duration:
                    return [max(slots1[0][0], slots2[0][0]), max(slots1[0][0], slots2[0][0]) +duration]
            elif slots1[0][1] < slots2[0][1]:
                slots1.pop(0)
            else:
                slots2.pop(0)
        return []


s = Solution()
s.meetingScheduler(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]],duration = 12)
s.meetingScheduler(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]],duration = 8)
