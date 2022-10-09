class Solution:
    def climbStairs(self, n: int) -> int:
#======== <Solution 1>: Combinations with Replacement ========#
        import math
        twos, ones = divmod(n, 2)
        ans = 0
        while twos >= 0:
            ans += math.factorial(ones + twos) // (math.factorial(ones) * math.factorial(twos))
            twos -= 1
            ones += 2
        return ans

#======== <Solution 2>: Fibonacci Sequence - Bottom-up ========#
        if n < 3: return n
        prev, curr = 1, 2
        for _ in range(2, n):
            prev, curr = curr, prev + curr
        return curr

#======== <Solution 3>: Fibonacci Formula ========#
        # Reference: https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
        import math
        return int((pow((1 + math.sqrt(5)) / 2, n + 1) - pow((1 - math.sqrt(5)) / 2, n + 1)) / math.sqrt(5))

# Reference: https://leetcode.com/problems/climbing-stairs/discuss/1792723/Python-or-In-Depth-Walkthrough-%2B-Explanation-or-DP-Top-Down-%2B-Bottom-Up
#======== <Solution 4>: Dynamic Programming - Top-down with Memoization ========#
        def helper(n: int) -> int:
            if n not in memo:
                memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]
        memo = {1: 1, 2: 2}
        return helper(n)

#======== <Solution 5>: Dynamic Programming - Bottom-up ========#
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n - 1]
