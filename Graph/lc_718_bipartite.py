class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        '''
        # BFS
        n = len(graph)
        colors = [-1]*n
        for node in range(n):
            if colors[node] == -1:
                que = deque([node])
                colors[node] = 1
                while que:
                    cur = que.popleft()
                    for nxt in graph[cur]:
                        if colors[nxt] == -1:
                            colors[nxt] = colors[cur]^1
                            que.append(nxt)
                        elif colors[nxt] == colors[cur]:
                            return False
        return True
        '''
        
        # DFS
        n = len(graph)
        colors = [-1]*n
        for node in range(n):
            if colors[node] == -1:
                stack = [node]
                colors[node] = 1
                while stack:
                    cur = stack.pop()
                    for nxt in graph[cur]:
                        if colors[nxt] == -1:
                            colors[nxt] = colors[cur]^1
                            stack.append(nxt)
                        elif colors[nxt] == colors[cur]:
                            return False
        return True