
# https://leetcode.com/problems/jump-game-iv/solution/
# 55 I is different

# 1345. Jump Game IV 1306 III


class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            print(curs)
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]] = []

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1



##Bidirectional BFS
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])  # store layers from start
        visited = {0, n-1}
        step = 0

        other = set([n-1]) # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]] = []

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1


# 1306. Jump Game III
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """

        curs = [start]  # store current layers
        visited = {start}

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if arr[node] == 0:
                    return True


                # check neighbors
                for child in [node- arr[node], node + arr[node]]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex


        return False   

# 45. Jump Game II
class Solution(object):
    def jump(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        if n <= 1:
            return 0

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step


                # check neighbors
                for child in range(node- arr[node], node + arr[node] +1):
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1    

# 55. Jump Game

class Solution(object):
    def canJump(self, arr):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n <= 1:
            return True
        
        cur = 0
        maximum = arr[0]
        
        while maximum < len(arr):
            if maximum >= len(arr)-1:
                return True
            
            tmp_m = maximum
            for i in range(cur+1, maximum + 1):
                if i + arr[i] > maximum:
                    maximum = i + arr[i]
            cur = tmp_m
            if maximum <= cur:
                return False    
            
        return True



#!/usr/bin/env python
# coding: utf-8

# In[12]:Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.



def canJumpFromPosition(position, nums):
    if position == len(nums) - 1:
        return True;

    furthestJump = min(position + nums[position], len(nums) - 1)
    for nextPosition in range(position+1, furthestJump+1):
        if canJumpFromPosition(nextPosition, nums):
            return True;

    return False;

canJumpFromPosition(0, [2,3,1,1,4])
canJumpFromPosition(0, [3,2,1,0,4])


# In[15]:


def jg_dp(nums):
    mem = [False]*len(nums)
    mem[-1] = 1
    for i in range(len(nums)-2, -1, -1):
        fur = min(nums[i] + i, len(nums)-1)
        for j in range(i+1, fur+1):
            if mem[j] == True:
                mem[i] = True
                break
    return mem[0]

jg_dp([3,2,1,0,4])