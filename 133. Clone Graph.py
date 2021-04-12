133. Clone Graph


class Solution:
    def cloneGraph(self, node):
        visited = {}
        def dfs(cur):
            copy = Node(cur.val)
            visited.update({copy.val:copy})
            copy.neighbors = [visited[nb.val] if nb.val in visited 
                              else dfs(nb) for nb in cur.neighbors]
            return copy
			
        return dfs(node) if node else None




 #########################

 class Node:
    def __init__(self, d):
        self.data = d
        self.neighbors = []

def clone_rec(root, nodes_completed):
    if root == None:
        return None

    pNew = Node(root.data)
    nodes_completed[root] = pNew

    for p in root.neighbors:
        x = nodes_completed.get(p)
        if x == None:
            pNew.neighbors += [clone_rec(p, nodes_completed)]
        else:
            pNew.neighbors += [x]
    return pNew

def clone(root):
    nodes_completed = {}
    return clone_rec(root, nodes_completed)


# this is un-directed graph i.e.
# if there is an edge from x to y
# that means there must be an edge from y to x
# and there is no edge from a node to itself
# hence there can maximim of (nodes * nodes - nodes) / 2 edgesin this graph
def create_test_graph_undirected(nodes_count, edges_count):
    import random
    vertices = []
    for i in range(0, nodes_count):
        vertices += [Node(i)]

    all_edges = []
    for i in range(0, nodes_count):
        for j in range(i + 1, nodes_count):
            all_edges.append([i, j])

    random.shuffle(all_edges)

    for i in range(0, min(edges_count, len(all_edges))):
        edge = all_edges[i]
        vertices[edge[0]].neighbors += [vertices[edge[1]]]
        vertices[edge[1]].neighbors += [vertices[edge[0]]]

    return vertices
  

def print_graph(vertices):
    for n in vertices:
        print(str(n.data), end = ": {")
        for t in n.neighbors:
              print(str(t.data), end = " ")
    print()

def print_graph_rec(root, visited_nodes):
    if root == None or root in visited_nodes:
        return

    visited_nodes.add(root)

    print(str(root.data), end = ": {")
    for n in root.neighbors:
        print(str(n.data), end = " ")
    print("}")

    for n in root.neighbors:
        print_graph_rec(n, visited_nodes)

def print_graph(root):
    visited_nodes = set()
    print_graph_rec(root, visited_nodes)

def main():
    vertices = create_test_graph_undirected(7, 18)
    print_graph(vertices[0])
    cp = clone(vertices[0])
    print()
    print("After copy.")
    print_graph(cp)


main()