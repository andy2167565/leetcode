class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n, visited = len(grid), len(grid[0]), set()
        def dfs(i, j, prev):
            if (i, j) in visited:  # Reached the end of a cycle
                return True
            visited.add((i, j))
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if m > x >= 0 <= y < n and (x, y) != prev and grid[x][y] == grid[i][j] and dfs(x, y, (i, j)):
                    return True
            return False
        return any((i, j) not in visited and dfs(i, j, None) for i in range(m) for j in range(n))
