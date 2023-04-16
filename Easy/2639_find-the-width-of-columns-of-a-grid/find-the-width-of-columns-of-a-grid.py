class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
#======== <Solution 1> ========#
        ans = [0] * len(grid[0])
        for row in grid:
            for i, num in enumerate(row):
                ans[i] = max(ans[i], len(str(num)))
        return ans

#======== <Solution 2> ========#
        return [max(len(str(num)) for num in col) for col in zip(*grid)]
