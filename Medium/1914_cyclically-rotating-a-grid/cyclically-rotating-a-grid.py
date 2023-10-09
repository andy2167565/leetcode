class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#======== <Solution 1> ========#
        m, n = len(grid), len(grid[0])
        top = [num for num in grid[0]]
        right = [row[-1] for row in grid[1:-1]]
        bottom = [num for num in grid[-1]][::-1]
        left = [row[0] for row in grid[1:-1]][::-1]
        vals = top + right + bottom + left
        inner = [[num for num in row[1:-1]] for row in grid[1:-1]]
        rotate = k % len(vals)
        vals = vals[rotate:] + vals[:rotate]
        if inner and inner[0]:
            inner = self.rotateGrid(inner, k)
        top = vals[:n]
        right = vals[n: n + m - 2]
        bottom = vals[n + m - 2: n + m - 2 + n][::-1]
        left = vals[n + m - 2 + n:][::-1]
        return [top] + [[a] + b + [c] for a, b, c in zip(left, inner, right)] + [bottom]

#======== <Solution 2> ========#
        import collections
        m, n = len(grid), len(grid[0])
        for r in range(min(m, n) // 2):
            vals = collections.deque()
            for j in range(r, n - r - 1):  # Collect top
                vals.append(grid[r][j])
            for i in range(r, m - r - 1):  # Collect right
                vals.append(grid[i][n - r - 1])
            for j in range(n - r - 1, r, -1):  # Collect bottom
                vals.append(grid[m - r - 1][j])
            for i in range(m - r - 1, r, -1):  # Collect left
                vals.append(grid[i][r])
            for _ in range(k % len(vals)):  # Rotate
                vals.append(vals.popleft())
            for j in range(r, n - r - 1):  # Fill top
                grid[r][j] = vals.popleft()
            for i in range(r, m - r - 1):  # Fill right
                grid[i][n - r - 1] = vals.popleft()
            for j in range(n - r - 1, r, -1):  # Fill bottom
                grid[m - r - 1][j] = vals.popleft()
            for i in range(m - r - 1, r, -1):  # Fill left
                grid[i][r] = vals.popleft()
        return grid
