class Solution:
    def fib(self, n: int) -> int:
#======== <Solution 1> ========#
        if n < 2: return n
        return self.fib(n - 1) + self.fib(n - 2)

#======== <Solution 2>: Fibonacci Sequence - Bottom-up ========#
        if n < 2: return n
        prev, curr = 0, 1
        for _ in range(1, n):
            prev, curr = curr, prev + curr
        return curr

#======== <Solution 3>: Fibonacci Formula ========#
        # Reference 1: https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
        # Reference 2: https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        import math
        return int((pow((1 + math.sqrt(5)) / 2, n) - pow((1 - math.sqrt(5)) / 2, n)) / math.sqrt(5))

# Reference: https://leetcode.com/problems/climbing-stairs/discuss/1792723/Python-or-In-Depth-Walkthrough-%2B-Explanation-or-DP-Top-Down-%2B-Bottom-Up
#======== <Solution 4>: Dynamic Programming - Top-down with Memoization ========#
        def helper(n: int) -> int:
            if n not in memo:
                memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]
        memo = {0: 0, 1: 1}
        return helper(n)

#======== <Solution 5>: Dynamic Programming - Bottom-up ========#
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]
