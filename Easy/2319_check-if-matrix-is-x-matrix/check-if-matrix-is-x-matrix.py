class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if not grid[i][j]:
                        return False
                elif grid[i][j]:
                    return False
        return True
