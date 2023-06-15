'''
A strongly connected component is the portion of a directed graph in which there is a path from each vertex to another vertex
Three steps to find the SCC:
1. Create an empty stack and Perform DFS traversal to push vertices into the stack.
2. Reverse the original graph
3. Perform DFS on the reverse graph from the top vertex of the stack
Traverse through all of its child vertices.
Once the already visited vertex is reached, one strongly connected component is formed.
'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices  # number of vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    # DFS
    def dfs(self,v,visited):
        visited[v] = True
        print(v,end='')
        # search each child vertices of v recursively
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i,visited)

    # fill in the stack
    def fill_stack(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_stack(i,visited,stack)
        stack = stack.append(v)



    # reverse the graph
    def reverse_graph(self):
        g = Graph(self.v)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    def get_SCC(self):
        stack = []
        visited = [False]*self.v

        # fill the stack
        for i in range(self.v):
            if not visited[i]:
                self.fill_stack(i,visited,stack)

        # Get the reversed graph
        g_reverse = self.reverse_graph()
        # Mark all the vertices as not visited (For second DFS)
        visited = [False]*self.v

        while stack:
            node = stack.pop()
            if not visited[node]:
                g_reverse.dfs(node,visited)
                print('')


if __name__=='__main__':
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 0)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(6, 7)

    print("Following are strongly connected components " +
          "in given graph")
    g.get_SCC()