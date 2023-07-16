class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#======== <Solution 1> ========#
        import collections, functools
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a] += b,
        @functools.cache
        def dfs(i, j):
            return i == j or any(dfs(k, j) for k in graph[i])
        return [dfs(u, v) for u, v in queries]

#======== <Solution 2> ========#
        graph = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
        return [graph[u][v] for u, v in queries]

#======== <Solution 3> ========#
        import collections
        graph, indegree, pres = collections.defaultdict(list), [0] * numCourses, [set() for _ in range(numCourses)]
        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            pres[course].add(pre)
        queue = collections.deque(course for course, degree in enumerate(indegree) if not degree)
        while queue:
            pre = queue.popleft()
            for course in graph[pre]:
                pres[course] |= pres[pre]
                indegree[course] -= 1
                if not indegree[course]:
                    queue.append(course)
        return [pre in pres[course] for pre, course in queries]
