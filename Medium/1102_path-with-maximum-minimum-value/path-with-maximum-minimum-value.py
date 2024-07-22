class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/path-with-maximum-minimum-value/solutions/325130/python-clean-priority-queue-similar-to-778/
        import heapq
        m, n = len(grid), len(grid[0])
        pq, score, grid[-1][-1] = [(-grid[-1][-1], m - 1, n - 1)], grid[0][0], -1
        while pq:
            val, i, j = heapq.heappop(pq)  # Get the neighboring cell with the largest value for the next step
            score = min(-val, score)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if not (x or y):  # Reached the starting point
                    return score
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    heapq.heappush(pq, (-grid[x][y], x, y))
                    grid[x][y] = -1  # Marked as visited
