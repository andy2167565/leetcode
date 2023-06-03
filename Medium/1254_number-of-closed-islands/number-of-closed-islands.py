class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
#======== <Solution 1> ========#
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j]:
                return 1
            grid[i][j] = 1  # Mark as visited
            return dfs(i, j - 1) * dfs(i, j + 1) * dfs(i - 1, j) * dfs(i + 1, j)
        return sum(dfs(i, j) for i in range(m) for j in range(n) if not grid[i][j])

#======== <Solution 2> ========#
        m, n, visited = len(grid), len(grid[0]), set()
        def bfs(i, j):
            visited.add((i, j))
            q, closed = [(i, j)], 1
            for i, j in q:
                for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if r < 0 or r >= m or c < 0 or c >= n:
                        closed = 0
                    elif not grid[r][c] and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
            return closed
        return sum(bfs(i, j) for i in range(m) for j in range(n) if not grid[i][j] and (i, j) not in visited)
