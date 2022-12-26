class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
# Reference: https://leetcode.com/problems/course-schedule-ii/solutions/1642354/c-python-simple-solutions-w-explanation-topological-sort-using-bfs-dfs/
#======== <Solution 1> ========#
        import collections
        graph, indegree, q, ans = collections.defaultdict(list), [0] * numCourses, collections.deque(), []  # indegree denotes the number of incoming edges to a node i.e. the number of prerequisites of a node
        for nxt, pre in prerequisites:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        for i in range(numCourses):  # Initialize and fill up a queue with all courses having 0 prerequisites
            if not indegree[i]:
                q.append(i)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nextCourse in graph[cur]:
                indegree[nextCourse] -= 1  # A prerequisite of nextCourse has been taken, which is cur
                if not indegree[nextCourse]:  # No prerequisite required
                    q.append(nextCourse)
        return ans if len(ans) == numCourses else []

#======== <Solution 2> ========#
        import collections
        graph, indegree, ans = collections.defaultdict(list), [0] * numCourses, []
        for nxt, pre in prerequisites:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        def dfs(cur):
            ans.append(cur)
            indegree[cur] = -1  # Marked as visited
            for nextCourse in graph[cur]:
                indegree[nextCourse] -= 1
                if not indegree[nextCourse]:
                    dfs(nextCourse)
        for i in range(numCourses):
            if not indegree[i]:
                dfs(i)
        return ans if len(ans) == numCourses else []
