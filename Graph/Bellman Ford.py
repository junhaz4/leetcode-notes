"""
Bellman-Ford algorithm works by overestimating the length of the path from the starting vertex to all other vertices.
Then it iteratively relaxes those estimates by finding new paths that are shorter than the previously overestimated paths.

function bellmanFord(G, S)
  for each vertex V in G
    distance[V] <- infinite
      previous[V] <- NULL
  distance[S] <- 0

  for each vertex V in G
    for each edge (U,V) in G
      tempDistance <- distance[U] + edge_weight(U, V)
      if tempDistance < distance[V]
        distance[V] <- tempDistance
        previous[V] <- U

  for each edge (U,V) in G
    If distance[U] + edge_weight(U, V) < distance[V}
      Error: Negative Cycle Exists

  return distance[], previous[]
"""
class Graph:
    def __init__(self,vertices):
        self.v = vertices # number of vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.v):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):
        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.v
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        # The term relaxation means updating the cost of all vertices connected to a vertex v
        # if those costs would be improved by including the path via vertex v
        for i in range(self.v-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)

g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)



