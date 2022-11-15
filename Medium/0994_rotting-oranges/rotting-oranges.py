class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        import collections
        m, n, fresh_count, ans = len(grid), len(grid[0]), 0, 0
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rotten = collections.deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        while rotten and fresh_count:
            ans += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for x, y in neighbors:
                    nr, nc = r + x, c + y
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        rotten.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh_count -= 1
        return ans if not fresh_count else -1
