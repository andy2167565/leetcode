class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans, top_sum, bottom_sum = float('inf'), sum(grid[0]), 0
        for top, bottom in zip(grid[0], grid[1]):  # Iterate the turning point of the first robot
            top_sum -= top
            ans = min(ans, max(top_sum, bottom_sum))  # Max for the second robot and min for the first robot
            bottom_sum += bottom
        return ans
