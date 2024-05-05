class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def move(i, j):
            for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                if 0 <= i + di < n and 0 <= j + dj < n:
                    yield i + di, j + dj

        def dfs(i, j, index):
            grid[i][j], area = index, 1  # Include grid[i][j] itself
            for ni, nj in move(i, j):
                if grid[ni][nj] == 1:
                    area += dfs(ni, nj, index)
            return area

        # Traverse every 1 cell and give it an index of island
        n, index, areas, coast = len(grid), 2, {0: 0}, set()  # Include area 0 in case all cells are 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j, index)
                    index += 1
                elif grid[i][j] == 0:
                    coast.add((i, j))

        # Traverse every 0 cell and count biggest island it can connect
        ans = max(areas.values())
        for i, j in coast:
            connected = set(grid[ni][nj] for ni, nj in move(i, j))
            ans = max(ans, sum(areas[index] for index in connected) + 1)  # Add grid[i][j] itself
        return ans
