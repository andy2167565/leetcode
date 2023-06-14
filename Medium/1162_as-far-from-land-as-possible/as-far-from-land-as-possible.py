class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/as-far-from-land-as-possible/solutions/3166138/day-41-c-bfs-easiest-beginner-friendly-approach-o-n-2-time-and-o-n-2-approach/
        import collections
        n, ans = len(grid), -1
        q = collections.deque([(i, j) for i in range(n) for j in range(n) if grid[i][j]])  # Collect all land cells
        if 0 < len(q) < n * n:  # The grid consists of both water cells and land cells
            while q:
                ans += 1
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        i, j = x + dx, y + dy
                        if 0 <= i < n and 0 <= j < n and not grid[i][j]:
                            grid[i][j] = 1  # Marked as visited
                            q.append((i, j))
        return ans
