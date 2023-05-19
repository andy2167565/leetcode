class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
#======== <Solution 1> ========#
        ans, prev_rows = 0, []
        for row in grid:
            curr_ones = {i for i, num in enumerate(row) if num}
            for prev_ones in prev_rows:
                matches = len(curr_ones & prev_ones)
                ans += matches * (matches - 1) // 2
            prev_rows.append(curr_ones)
        return ans

#======== <Solution 2> ========#
        ans, m, n = 0, len(grid), len(grid[0])
        for row1 in range(m - 1):
            for row2 in range(row1 + 1, m):
                matches = 0
                for col in range(n):
                    if grid[row1][col] and grid[row2][col]:
                        ans += matches
                        matches += 1
        return ans

#======== <Solution 3> ========#
        import itertools, numpy as np
        return sum(sum(range((row1 & row2).sum())) for row1, row2 in itertools.combinations(np.array(grid), 2))
