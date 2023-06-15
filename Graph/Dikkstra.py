"""
Dijkstra’s Algorithm can only be used on graphs with non-negative weights of all edges to find single source shortest path
function Dijkstra(Graph, source):
 2
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v] and dist[u] is not INFINITY:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
"""
from collections import defaultdict
import heapq
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = defaultdict(dict)

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self,graph,start):
        dist = {v: float('inf') for v in range(graph.v)}
        dist[start] = 0
        visited = set()
        queue = [(0, start)]
        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            for nei, nei_cost in self.edges[node].items():
                if nei in visited:
                    continue
                new_cost = nei_cost+cost
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(queue, (new_cost,nei))
        return dist




