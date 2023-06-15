# lc 1360

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque, defaultdict

def dfs(cur, graph):
    # a helper function used to print the graph result
    if len(graph[cur]) == 0:
        return '(' + cur + ')'
    left = ''
    right = ''
    if len(graph[cur]) >= 1:
        left = dfs(graph[cur][0], graph)
    if len(graph[cur]) >= 2:
        right = dfs(graph[cur][1], graph)
    return '(' + cur + left + right + ')'


def main():
    '''
    The idea is to build a topological ordering of the input graph and check if errors exist
    '''
    for line in sys.stdin:
        error_list = []  # store the error code
        seen = set()  # store already visited tuples
        pairs = line.split(' ')  # convert the input into a list
        indegree = defaultdict(int)  # store the indegree of each node
        graph = defaultdict(list)  # store the graph using a dictonary
        nodes = set()  # store all nodes

        for p in pairs:
            # check the format of each tuple
            if len(p) != 5 or p[0] != '(' or p[4] != ')' or p[2] != ",":
                error_list.append('E1')

            # check if a tuple is visited multiple times
            if p in seen:
                error_list.append('E2')
            else:
                seen.add(p)
            parent, child = p[1], p[3]
            nodes.add(parent)
            nodes.add(child)
            graph[parent].append(child)

            # check if a parent has more than two children
            if len(graph[parent]) > 2:
                error_list.append('E3')
            indegree[child] += 1

            # check if a node has multiple roots
            if indegree[child] > 1:
                error_list.append('E4')

        # store the node with indegree = 0 into que
        que = deque()
        for v in nodes:
            if indegree[v] == 0:
                que.append(v)

        # if the que contains more than 1 element, that means multiple roots
        if len(que) > 1:
            error_list.append('E4')

        order = []  # store the topological order
        count = 0  # store the number of nodes visited
        while que:
            node = que.popleft()
            order.append(node)
            count += 1
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)

        # this means a cycle exists since we cannot visit all nodes
        if count != len(graph):
            error_list.append('E5')

        # if error_list not empty, the errors are present and print the first listed error
        if error_list:
            error_list.sort()
            error = error_list[0]
            sys.stdout.write(error)
        else:
            # if no errors, print the graph in the required format
            root = order[0]
            res = dfs(root, graph)
            sys.stdout.write(res)


main()