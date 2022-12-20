class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        import collections
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '*':  # Our location is found and then start traversing
                    q = collections.deque()
                    q.append((r, c, 0))
                    grid[r][c] = 'X'  # Marked as visited
                    while q:
                        r, c, step = q.popleft()
                        for dr, dc in directions:
                            row, col = r + dr, c + dc
                            if 0 <= row < m and 0 <= col < n and grid[row][col] != 'X':
                                if grid[row][col] == '#':  # Food is found
                                    return step + 1
                                q.append((row, col, step + 1))
                                grid[row][col] = 'X'
        return -1
