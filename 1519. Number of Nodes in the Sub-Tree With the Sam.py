# 1519. Number of Nodes in the Sub-Tree With the Same Label


# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/discuss/1221797/Python-3%3A-O(n)-beats-100.
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        def dfs(node, adjList, dic, res, visited):
            already = dic[labels[node]]
            dic[labels[node]] += 1
            visited.add(node)
            for nei in adjList[node]:
                if nei in visited: 
                    continue
                dfs(nei, adjList, dic, res, visited)
            
            res[node] = dic[labels[node]] - already

            
        res = [0]*n
        adjList = collections.defaultdict(list)
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src). #src is not alway parent

        dfs(0, adjList, collections.defaultdict(int), res, set())
        
        return res



# facebook: Nodes in a Subtree (above problem asking number that has same label as the given node, this may ask for different labels; can we modify above to save count for all letters)
# You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
# You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.
class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

# Add any helper functions you may need here


def count_of_nodes(root, queries, s):
  # Write your code here
    ans = []
    for query in queries:
        ans.append(count_node(root, query, s))
        
    return ans

    
def count_node(root, query, s):
    
    q = [root]

    ans = 0
    flag = False
    while q:
        tmp_q = []
        for node in q:
            if node.val == query[0]:
                flag = True
                if s[node.val-1] == query[1]:
                    ans += 1
                q = node.children
                break
            else:
                tmp_q = tmp_q[:] + node.children[:]
        if flag:
            break
        else:
            q = tmp_q[:]
            
    while q:
        tmp_q = []
        for node in q:
            if s[node.val - 1] == query[1]:
                ans += 1
            tmp_q = tmp_q[:] + node.children[:]
        
        q = tmp_q[:]
    return ans  