class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        m, n, visited = len(grid), len(grid[0]), set()
        goal = (m - 1, n - 1)
        def dfs(i, j):
            if (i, j) == goal:
                return True
            visited.add((i, j))
            for di, dj in directions[grid[i][j]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and (-di, -dj) in directions[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            return False
        return dfs(0, 0)
