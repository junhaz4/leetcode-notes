'''
There are two ways to represent graph: Adjacency Matrix vs Adjacency List

1. Adjacency Matrix: An adjacency matrix is a way of representing a graph as a matrix of booleans (0's and 1's).
A finite graph can be represented in the form of a square matrix on a computer,
where the boolean value of the matrix indicates if there is a direct path between two vertices.

2. Adjacency List: An adjacency list represents a graph as an array of linked lists.
The index of the array represents a vertex and each element in its linked list represents
the other vertices that form an edge with the vertex.
'''

# Adjacency Matrix Implementation
class Graph(object):
    def __init__(self,size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def __len__(self):
        return self.size

    def add_edge(self,u,v):
        if u == v:
            print('same vertex')
        self.adjMatrix[u][v] = 1
        self.adjMatrix[v][u] = 1

    def remove_edge(self,u,v):
        if self.adjMatrix[u][v]==0:
            print('no such edge exists')
            return
        self.adjMatrix[u][v] = 0
        self.adjMatrix[v][u] = 0

def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    print(g.adjMatrix)


# Adjacency List Implementation

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()