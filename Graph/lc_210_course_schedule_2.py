import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # method 1 kahn's algorithm BFS
        courses = {n: [] for n in range(numCourses)}
        for cur, prev in prerequisites:
            courses[cur].append(prev)

        indegree = [0]*numCourses
        for cur,prev in courses.items():
            indegree[cur] += len(prev)

        que = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)

        count = 0
        course_order = []
        while que:
            course = que.popleft()
            course_order.append(course)
            for cur, prev in courses.items():
                if course in prev:
                    indegree[cur] -= 1
                    if indegree[cur] == 0:
                        que.append(cur)
            count += 1

        if count == numCourses:
            return course_order
        else:
            return []

# method 2 DFS
def findOrder(self, numCourses: int, prerequisites):
    courses = {n: [] for n in range(numCourses)}
    for cur, prev in prerequisites:
        courses[cur].append(prev)

    visited, cycle = set(), set()
    top_order = []

    def dfs(course):
        if course in cycle:
            return False
        if course in visited:
            return True
        cycle.add(course)
        for prev in courses[course]:
            if dfs(prev) == False:
                return False
        cycle.remove(course)
        visited.add(course)
        top_order.append(course)
        return True

    for i in range(numCourses):
        if dfs(i) == False:
            return []
    return top_order
