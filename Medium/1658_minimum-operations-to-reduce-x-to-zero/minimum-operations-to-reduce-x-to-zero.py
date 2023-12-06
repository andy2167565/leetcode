class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix, dp = 0, [0]  # dp[i]: sum(nums[:i])
        for num in nums:
            prefix += num
            dp.append(prefix)
        rest, target, seen = -1, sum(nums) - x, {v: i for i, v in enumerate(dp)}
        for v, i in seen.items():  # Find subarrays that have sum equal to target
            if v + target in seen:
                rest = max(seen[v + target] - i, rest)  # The number of values left after removal
        return rest if rest == -1 else len(nums) - rest
