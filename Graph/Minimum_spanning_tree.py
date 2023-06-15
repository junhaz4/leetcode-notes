"""
Spanning tree
A spanning tree is a sub-graph of an undirected connected graph, which includes all the vertices of the graph
with a minimum possible number of edges. If a vertex is missed, then it is not a spanning tree.

Minimum Spanning Tree?
The cost of the spanning tree is the sum of the weights of all the edges in the tree. There can be many spanning trees.
Minimum spanning tree is the spanning tree where the cost is minimum among all the spanning trees.
There also can be many minimum spanning trees.
The number of edges |E| = |V|-1

#### Prim’s Algorithm (BFS+Min Heap)
Prim’s Algorithm also use Greedy approach to find the minimum spanning tree.
In Prim’s Algorithm we grow the spanning tree from a starting position.
Unlike an edge in Kruskal's, we add vertex to the growing spanning tree in Prim's.
Time complexity: O(|E|log|V|)
Steps:
1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree
3. Keep repeating step 2 until we get a minimum spanning tree

#### Kruskal's Algorithm (UNION-FIND)
Kruskal’s Algorithm builds the spanning tree by adding edges one by one into a growing spanning tree.
Also follows greedy approach as in each iteration it finds an edge which has least weight and add it to the growing spanning tree.
Time complexity: O(|E|log|E|)
Steps:
1. Sort the graph edges with respect to their weights.
2. Start adding edges to the MST from the edge with the smallest weight until the edge of the largest weight.
3. Only add edges which doesn't form a cycle , edges which connect only disconnected components.
"""

### Prim's Algorithm

v = 5 # number of vertices
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
visited = [False]*v  # create a array to track selected vertex
no_edges = 0  # the number of egdse in MST = V-1
visited[0] = True  # choose 0th vertex and make it true
while no_edges < v-1:
    # For every vertex in the set S, find the all adjacent vertices calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise choose another vertex nearest to selected vertex  at step 1.
    minimum = float("inf")
    x, y = 0, 0
    for i in range(v):
        # If the node is part of the MST, look its relationships
        if visited[i]:
            for j in range(v):
                # not in selected and there is an edge
                if not visited[j] and G[i][j]:
                    if minimum>G[i][j]:
                        minimum = G[i][j]
                        x,y = i,j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    no_edges += 1
    visited[y] = True


### Kruskal's algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = [i for i in range(self.V)]
        self.rank = [0 for i in range(self.V)]


    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self,i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

    def kruskalAlgo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(u)
            y = self.find(v)
            if x!=y:
                e += 1
                result.append([u, v, w])
                self.union(x,y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))





