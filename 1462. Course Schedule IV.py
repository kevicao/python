1462. Course Schedule IV

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prereq = dict()
        for pre in prerequisites:
            if pre[0] in prereq:
                prereq[pre[0]].append( pre[1])
            else:
                prereq[pre[0]] = [pre[1]]
        
        lookup = dict()
        for pre in prereq.keys():
            lookup[pre] = prereq[pre][:]
            queue = prereq[pre][:]
            while len(queue) > 0:
                tmp = queue.pop(0)
                if tmp in prereq:
                    lookup[pre] = lookup[pre][:] + prereq[tmp][:]
                    queue = queue[:] + prereq[tmp][:]
                    
  
        ans = []
        for query in queries:
            if query[0] not in lookup:
                ans.append(False)
            else:
                if query[1] in lookup[query[0]]:
                    ans.append(True)
                else:
                    ans.append(False)
                
        return ans
         