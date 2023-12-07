class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        memo = {}
        def dfs(num, base):
            if not num:
                return 1
            if num < 0 or base > n or base**x > num:
                return 0
            if (num, base) in memo:
                return memo[(num, base)]
            memo[(num, base)] = dfs(num - base**x, base + 1) + dfs(num, base + 1)  # Include current base or not
            return memo[(num, base)]
        return dfs(n, 1) % (10**9 + 7)
