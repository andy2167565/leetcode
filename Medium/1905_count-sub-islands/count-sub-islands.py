class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#======== <Solution 1> ========#
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid2[i][j]:
                grid2[i][j] = 0
                for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                    dfs(i + di, j + dj)
        m, n, ans = len(grid1), len(grid1[0]), 0
        for i in range(m):  # Remove islands in grid2 that do not share all land cells in grid1
            for j in range(n):
                if grid2[i][j] and not grid1[i][j]:
                    dfs(i, j)
        for i in range(m):  # Count sub-islands
            for j in range(n):
                if grid2[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans

#======== <Solution 2> ========#
        m, n = len(grid1), len(grid1[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid2[i][j]:
                grid2[i][j], sub = 0, grid1[i][j]
                for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                    sub &= dfs(i + di, j + dj)
                return sub
            return 1
        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid2[i][j])
