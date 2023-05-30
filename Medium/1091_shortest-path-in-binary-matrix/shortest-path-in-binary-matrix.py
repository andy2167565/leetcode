class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        import collections
        n = len(grid)
        if not (grid[0][0] or grid[n - 1][n - 1]):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            queue, visited = collections.deque([(0, 0, 1)]), {(0, 0)}
            while queue:
                i, j, l = queue.popleft()
                if (i, j) == (n - 1, n - 1):
                    return l
                for di, dj in directions:
                    x, y = i + di, j + dj
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited and not grid[x][y]:
                        visited.add((x, y))
                        queue.append((x, y, l + 1))
        return -1
