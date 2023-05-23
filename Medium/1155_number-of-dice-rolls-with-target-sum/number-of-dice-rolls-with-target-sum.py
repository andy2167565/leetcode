class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
# Reference: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/solutions/355894/python-dp-with-memoization-explained/
#======== <Solution 1> ========#
        memo = {}
        def dfs(n, target):
            if not n:  # Dices have run out
                return int(not target)  # Check if we have reached target
            if (n, target) not in memo:
                memo[n, target] = sum(dfs(n - 1, t) for t in range(max(0, target - k), target))  # Count the number of ways to reach target with n dices
            return memo[n, target]
        return dfs(n, target) % (10**9 + 7)

#======== <Solution 2> ========#
        import functools
        @functools.cache
        def dfs(n, target):
            if not n:
                return int(not target)
            if target <= 0:
                return 0
            return sum(dfs(n - 1, target - num) for num in range(1, k + 1))
        return dfs(n, target) % (10**9 + 7)

# Reference: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/solutions/355850/python-dp-solution-similar-to-coin-change/comments/351932
#======== <Solution 3> ========#
        dp = [1] + [0] * target  # dp[i]: Number of ways to reach target i
        for _ in range(n):  # Go through each throw of n dices
            for t in range(target, -1, -1):
                dp[t] = sum(dp[max(0, t - k):t])  # Count the number of ways to reach target t with current number of dices
        return dp[target] % (10**9 + 7)
