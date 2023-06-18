class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        import functools
        n, MOD = len(nums), 10**9 + 7
        @functools.cache
        def dfs(prev, mask):
            if mask == (1 << n) - 1:
                return 1
            count = 0
            for i in range(n):
                if not (mask & (1 << i)) and (not nums[i] % prev or not prev % nums[i]):
                    count += dfs(nums[i], mask | (1 << i))
            return count % MOD
        return dfs(1, 0)
