'''
A topological sort gives an order in which to perform the jobs.
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices,
such that for every directed edge {u,v} vertex u comes before v in the ordering
'''

from collections import defaultdict
class Graph:

    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices #number of nodes

    def add_edge(self,u,v):
        self.graph[u].append(v)

# Kahn's Algorithm
def topological_sort(graph):

    # graph is represented by a list of list
    size = len(graph)
    in_degree = [0]*size

    # get indegree of the graph
    for i in graph:
        for j in graph[i]:
            in_degree[j] += 1

    # queue storing nodes with non-dependencies
    queue = []
    for i in range(size):
        if in_degree[i] == 0:
            queue.append(i)

    # get topological order
    top_order = []
    count = 0
    while queue:
        u = queue.pop(0)
        top_order.append(u)
        count += 1
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if count != size:
        print ("There exists a cycle in the graph")
    else:
        return top_order