'''
The BFS algorithm works as follows:
1. Start by putting any one of the graph's vertices at the back of a queue.
2. Take the front item of the queue and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
4. Keep repeating steps 2 and 3 until the queue is empty.
'''



from collections import deque
def BFS(graph,root):
    visited = set()
    queue = deque([root])
    visited.add(root)
    while queue:
        cur = queue.popleft()
        print(cur)
        for v in graph[cur]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    BFS(graph, 0)