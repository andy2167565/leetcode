class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
# Reference: https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation/60058
        import collections
        pre_dict = collections.defaultdict(list)
        visited = [0] * numCourses
        for a, b in prerequisites:
            pre_dict[a].append(b)  # The prerequisites of a are pre_dict[a]
        def dfs(i):
            if visited[i] == -1:  # A cycle exists if course i is marked as visited while its neighbors have not done visited yet
                return False
            if visited[i] == 1:  # Course i and its neighbors have done visted
                return True
            visited[i] = -1  # Mark course i as visited
            if any(not dfs(j) for j in pre_dict[i]):  # Visit all the neighbors
                return False
            visited[i] = 1  # After visiting all the neighbors, mark it as done visited
            return True
        return all(dfs(i) for i in range(numCourses))

#======== <Solution 2> ========#
        import collections
        pre_dict = collections.defaultdict(list)
        visited = set()  # Courses visited while their neighbors have not done visited yet
        for a, b in prerequisites:
            pre_dict[a].append(b)
        def haveCycle(i, processing):
            if i in visited:
                if i in processing:  # Course i is being processed, which indicates a cycle exists
                    return True
                return False  # Course i have been processed
            visited.add(i)  # Mark course i as visited
            processing.append(i)  # Add it to the current stack
            for j in pre_dict[i]:
                if haveCycle(j, processing):
                    return True
            processing.pop()  # Once finished processing, we pop it out of the stack
            return False
        return not any(haveCycle(i, []) for i in range(numCourses))

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/course-schedule/discuss/162743/JavaC++Python-BFS-Topological-Sorting-O(N-+-E)/917532
        pre_list = [[] for _ in range(numCourses)]
        need = [0] * numCourses
        for a, b in prerequisites:
            pre_list[b].append(a)  # Each b is the prerequisite of a's in pre_list[b]
            need[a] += 1  # Number of courses needed to take before taking a
        bfs = [i for i in range(numCourses) if not need[i]]  # Index of courses without any prerequisite
        for pre in bfs:  # Courses in bfs become the prerequisites of other courses
            for course in pre_list[pre]:  # Loop through the courses that need pre as a prerequisite
                need[course] -= 1  # Decrement pre in need
                if not need[course]:  # If there is no other prerequisite needed for the course
                    bfs.append(course)  # Append it to bfs as a prerequisite for further searching
        # Courses are stored in bfs if no prerequisite left for each of them
        # Check if the number of courses fully visited is equal to numCourses
        return len(bfs) == numCourses

#======== <Solution 4> ========#
        import collections
        pre_list = [[] for i in range(numCourses)]
        degrees = [0] * numCourses
        for course, pre_course in prerequisites:
            pre_list[pre_course].append(course)
            degrees[course] += 1
        queue = collections.deque(course for course, degree in enumerate(degrees) if not degree)
        while queue:
            course = queue.popleft()
            for next_course in pre_list[course]:
                degrees[next_course] -= 1
                if not degrees[next_course]:
                    queue.append(next_course)
        return not sum(degrees)  # sum(degrees) > 0 if there are courses left without being fully visited
