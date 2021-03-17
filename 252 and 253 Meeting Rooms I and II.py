# 253. Meeting Rooms II

# find the number of room needed to schedule all jobs

# https://medium.com/@edward.zhou/leetcode-253-meeting-rooms-ii-explained-python3-solution-3f8869612df

class Solution(object):
    def meetingRoom(self, intervals):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        startTimes = [x[0] for x in intervals]
        endTimes = [x[1] for x in intervals]
        startTimes = sorted(startTimes)
        endTimes = sorted(endTimes)
         
        room = 0
        
        while len(startTimes) > 0:
            startTime = startTimes.pop(0)
            if startTime > endTimes[0]:
                endTimes.pop(0)
            else:
                room +=1
            
        return room


s = Solution()
s.meetingRoom([(1,3),(9,18),(3,7),(6,12),(4,9)])


# 252. Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.

#just sort starting time and check with next one