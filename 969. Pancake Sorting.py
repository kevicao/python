# 969. Pancake Sorting
# reverse first i item each time to sort an array

# https://leetcode.com/problems/pancake-sorting/solution/

#find max, and flip to 1 position then to desired position; below code also assume elements are 1-n; similar to bubble sort (swap each pair if in wrong order)
#this wiki discuss gave the same solution https://en.wikipedia.org/wiki/Pancake_sorting
class Solution(object):
    def pancakeSort(self, A):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)  #assume the array is 1..n, otherwise need find the max value
        while value_to_sort > 0:
            # locate the position for the value to sort in this round
            index = A.index(value_to_sort)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if index != value_to_sort - 1:
                # flip the value to the head if necessary
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(value_to_sort)
                flip(A, value_to_sort)  #no matter where the max is, we need move max to desired position in second step

            # move on to the next round
            value_to_sort -= 1

        return ans



#facebook practice: Minimizing Permutations
# In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
# Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
# Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

# Create graph where each node is a permutation. Create an edge if the two permutations are reachable by one swap. Then find minimum path between the source P and target sorted(P) with dijkstra's algorithm.

import math
import heapq

def generate_graph(result, curr_num, next_num):
  if not next_num:
    result[tuple(curr_num)] = []
    
  for i in range(len(next_num)):
    generate_graph(result, curr_num+[next_num[i]], next_num[:i]+next_num[i+1:])

def dijkstra(graph, source, target):
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    dist = {}
    prev = {}
    
    q = []
    dist[source] = 0
    for node in graph.keys():
        if node != source:
            dist[node] = float('inf')
        heapq.heappush(q, (dist[node], node))
    
    while q:
        p,node = heapq.heappop(q)
        if p > dist[node]:
            continue
        for neighbor in graph[node]:
            alt = dist[node] + 1
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = node
                heapq.heappush(q, (alt, neighbor))
                
    return dist[target]
    
def minOperations(arr):
  graph = {}
  generate_graph(graph, [], sorted(arr))
  for node in graph.keys():
    for i in range(2, len(arr)+1):
      for j in range(0, len(arr)-i+1):
        neighbor = list(node)
        neighbor = neighbor[:j] + neighbor[j:j+i][::-1] + neighbor[j+i:]
        graph[node].append(tuple(neighbor))

  return dijkstra(graph,tuple(arr), tuple(sorted(arr)))
