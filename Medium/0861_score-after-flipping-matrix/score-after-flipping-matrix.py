class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/score-after-flipping-matrix/solutions/143722/c-java-python-easy-and-concise/
        m, n = len(grid), len(grid[0])
        ans = (1 << n - 1) * m
        for j in range(1, n):
            curr = sum(grid[i][j] == grid[i][0] for i in range(m))
            ans += max(curr, m - curr) * (1 << n - 1 - j)
        return ans
