class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n, directions = len(grid), len(grid[0]), [(0, 1), (0, -1), (1, 0), (-1, 0)]
        boundary, queue = [], [next((i, j) for i in range(m) for j in range(n) if grid[i][j])]  # First land cell in grid
        for i, j in queue:  # Collect the boundary cells of the first island i.e. the outermost land cells connected to the water cells
            grid[i][j] = -1  # Marked as visited
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if m > ni >= 0 <= nj < n and grid[ni][nj] != -1:
                    if grid[ni][nj]:
                        grid[ni][nj] = -1
                        queue.append((ni, nj))
                    else:
                        boundary.append((i, j))
        step = 0
        while boundary:
            next_boundary = []
            for i, j in boundary:
                grid[i][j] = -1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if m > ni >= 0 <= nj < n and grid[ni][nj] != -1:
                        if grid[ni][nj]:
                            return step
                        grid[ni][nj] = -1
                        next_boundary.append((ni, nj))
            step += 1
            boundary = next_boundary
