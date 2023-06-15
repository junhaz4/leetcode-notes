class Solution:
    def countComponents(self, n: int, edges) -> int:
        # method 1
        ranks = [1] * (n)
        parents = [i for i in range(n)]

        def find(x):
            while x != parents[x]:
                parents[x] = find(parents[x])
                x = parents[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return 0
            if ranks[rx] > ranks[ry]:
                parents[ry] = rx
                ranks[rx] += 1
            else:
                parents[rx] = ry
                ranks[ry] += 1
            return 1

        result = n
        for x, y in edges:
            result -= union(x, y)
        return result

# method 2
def countComponents(self, n: int, edges) -> int:
    ranks = [1] * (n)
    parents = [i for i in range(n)]

    def find(x):
        while x != parents[x]:
            parents[x] = find(parents[x])
            x = parents[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if ranks[rx] > ranks[ry]:
            parents[ry] = rx
            ranks[rx] += 1
        else:
            parents[rx] = ry
            ranks[ry] += 1
        return True

    for x, y in edges:
        union(x, y)

    result = set()
    for i in range(n):
        result.add(find(i))
    return len(result)