class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/solutions/288520/longest-path-in-dag/
        import collections
        m, n = len(matrix), len(matrix[0])
        indegree = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for r in range(m):
            for c in range(n):
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n:
                        if matrix[r][c] > matrix[row][col]:  # Assign gradient if there is an increasing trend
                            indegree[r][c] += 1
        queue = collections.deque()
        for r in range(m):
            for c in range(n):
                if not indegree[r][c]:  # Collect local minimum with indegree 0
                    queue.append((r, c))
        ans = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n:
                        if matrix[r][c] < matrix[row][col]:  # Find increasing trend
                            indegree[row][col] -= 1
                            if not indegree[row][col]:  # Keep expanding to next level
                                queue.append((row, col))
            ans += 1
        return ans
