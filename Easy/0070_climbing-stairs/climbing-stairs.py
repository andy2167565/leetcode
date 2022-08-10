class Solution:
    def climbStairs(self, n: int) -> int:
#======== <Solution 1>: Fibonacci Sequence - Bottom-up ========#
        if n < 3:
            return n
        a, b = 1, 2
        while n > 2:        
            a, b = b, a+b
            n -= 1
        return b
        
#======== <Solution 2>: Fibonacci Formula ========#
        return int((pow((1+sqrt(5))/2, n+1)-pow((1-sqrt(5))/2, n+1))/sqrt(5))
        
#======== <Solution 3>: Dynamic Programming ========#
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]
        
#======== <Solution 4>: Combinations with Replacement ========#
        from math import factorial
        ones = n % 2
        twos = n // 2
        result = 0
        while twos >= 0:
            result += factorial(ones + twos) // (factorial(ones) * factorial(twos))
            twos -= 1
            ones += 2
        return result
