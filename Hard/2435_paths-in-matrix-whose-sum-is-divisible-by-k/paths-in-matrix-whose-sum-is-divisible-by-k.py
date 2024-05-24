class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # Reference: https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/solutions/2678950/python-dp-solution/
        import collections
        n = len(grid[0])
        dp = [collections.Counter() for _ in range(n + 1)]  # dp[i][j]: The number of paths to get to (m - 1, i), with sum % k = j
        dp[0][0] = 1
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                dp[j] = collections.Counter({(num + key) % k: val % (10**9 + 7) for key, val in (dp[j] + dp[j - 1]).items()})
        return dp[n - 1][0]
