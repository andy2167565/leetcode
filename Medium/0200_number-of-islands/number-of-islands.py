class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#======== <Solution 1> ========#
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '#'  # Marked as visited
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans

#======== <Solution 2> ========#
        import collections
        m, n, ans = len(grid), len(grid[0]), 0
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = collections.deque([])
                    q.append((i, j))
                    ans += 1
                    grid[i][j] = '#'
                    while q:
                        row, col = q.popleft()
                        for x, y in neighbors:
                            nrow, ncol = row + x, col + y
                            if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == '1':
                                grid[nrow][ncol] = '#'
                                q.append((nrow, ncol))
        return ans
