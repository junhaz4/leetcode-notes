import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        '''
        Topological Sort By Kahn's algorithm(BFS)
        convert the prerequisites into a graph where each course is a node and
        a edge from x to y if x is a prerequisite for y
        '''
        # get the course graph {current-course:prerequisite-course}
        course_graph = {n: [] for n in range(numCourses)}
        for cur, prev in prerequisites:
            course_graph[cur].append(prev)

        # get the indegree for each course
        indegree = [0] * numCourses
        for cur, prev in course_graph.items():
            indegree[cur] += len(prev)

        # get queue for storing courses with no prerequisites
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # get topological order
        count = 0
        while queue:
            course = queue.popleft()
            for cur, prev in course_graph.items():
                if course in prev:
                    indegree[cur] -= 1
                    if indegree[cur] == 0:
                        queue.append(cur)
            count += 1

        if count == numCourses:
            return True
        else:
            return False

### Method 2 topological sort via DFS
def canFinish(self, numCourses, prerequisites) -> bool:
    # get the course graph {current-course:prerequisite-course}
    course_graph = {n: [] for n in range(numCourses)}
    for cur, prev in prerequisites:
        course_graph[cur].append(prev)

    # visited set store all courses along the current dfs path
    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if course_graph[course] == []:
            return True
        visited.add(course)
        for prev in course_graph[course]:
            if not dfs(prev):
                return False
        visited.remove(course)
        course_graph[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True
