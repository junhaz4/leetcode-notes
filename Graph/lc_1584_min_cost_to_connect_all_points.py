import heapq
# Prim's Algorithm (BFS+Min Heap)
# add vertex to the growing spanning tree in Prim's.
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        graph = {i:[] for i in range(n)}

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                cost = abs(x1-x2)+ abs(y1-y2)
                graph[i].append([cost,j])
                graph[j].append([cost,i])

        visited = set()
        res = 0
        minHeap = [[0,0]]

        while len(visited) != n:
            cost, node = heapq.heappop(minHeap)
            if node not in visited:
                res += cost
                visited.add(node)

                for nei_cost, nei in graph[node]:
                    if nei not in visited:
                        heapq.heappush(minHeap,[nei_cost,nei])
        return res

# Kruskal's Algorithm (Union Find)
def minCostConnectPoints(points: list[list[int]]) -> int:
    n = len(points)
    parents = [i for i in range(n)]
    ranks = [0 for i in range(n)]
    graph = []
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1,n):
            x2, y2 = points[j]
            cost = abs(x1-x2)+ abs(y1-y2)
            graph.append([i,j,cost])
    graph.sort(key=lambda item: item[2])

    def find(node):
        """
        if node == parents[node]:
            return node
        parents[node] = find(parents[node])
        return parents[node]
        """
        while node != parents[node]:
            parents[node] = find(parents[node])
            node = parents[node]
        return node

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if ranks[rx] > ranks[ry]:
            parents[ry] = rx
            ranks[rx] += 1
        else:
            parents[rx] = ry
            ranks[ry] += 1
        return True

    no_edges = 0
    min_cost = 0
    for cur, nxt, weight in graph:
        if union(cur, nxt):
            min_cost += weight
            no_edges += 1
            if no_edges == n - 1:
                break
    return min_cost
