class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        valid, visited = m * n, set()

        def backtrack(row, col):
            if len(visited) == valid and grid[row][col] == 2:  # Reached the ending square with all squares visited
                return 1
            ans = 0
            for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                r, c = row + dr, col + dc
                if m > r >= 0 <= c < n and (r, c) not in visited and grid[r][c] != -1:
                    visited.add((r, c))
                    ans += backtrack(r, c)
                    visited.remove((r, c))
            return ans

        for i in range(m):
            for j in range(n):
                match grid[i][j]:
                    case 1:  # Starting square
                        start = [i, j]
                        visited.add((i, j))
                    case -1:  # Obstacles
                        valid -= 1
        return backtrack(*start)
