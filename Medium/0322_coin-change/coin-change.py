class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
# Reference: https://leetcode.com/problems/coin-change/discuss/1475250/Python-4-solutions%3A-Top-down-DP-Bottom-up-DP-Space-O(amount)-Clean-and-Concise
#======== <Solution 1> ========#
        @cache
        def dp(i, amount):  # Minimum number of coins to make up amount with coins from index 0 to index i
            if not amount: return 0
            if i == -1: return float('inf')  # Out of the head of coins
            ans = dp(i - 1, amount)  # Skip i-th coin
            if amount >= coins[i]:  # Use i-th coin
                ans = min(ans, dp(i, amount - coins[i]) + 1)
            return ans
        ans = dp(len(coins) - 1, amount)
        return ans if ans != float('inf') else -1

#======== <Solution 2> ========#
        @cache
        def dp(amount):  # Minimum number of coins to make up amount
            if not amount: return 0
            ans = float('inf')
            for coin in coins:
                if amount >= coin:
                    ans = min(ans, dp(amount - coin) + 1)
            return ans
        ans = dp(amount)
        return ans if ans != float('inf') else -1

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/coin-change/discuss/1104246/Python-short-dp-O(amount*n)-solution-explained
        @cache
        def dp(amount):
            if not amount: return 0
            if amount < 0: return float('inf')
            return min(dp(amount - coin) + 1 for coin in coins)
        ans = dp(amount)
        return ans if ans != float('inf') else -1

#======== <Solution 4> ========#
        # Reference: https://leetcode.com/problems/coin-change/discuss/720880/Python-DP-Explanation-with-Pictures
        n = len(coins)
        dp = [[0] + [float('inf')] * amount for _ in range(n)]  # dp[i][j] is the minimum number of coins to make up amount j with coins from index 0 to index i
        for i in range(n):
            for j in range(1, amount + 1):  # For each coin, check if any amount is able to use it
                if i > 0:
                    dp[i][j] = dp[i - 1][j]  # Inherit the minimum number of coins for amount j in (i - 1)-th round to compare with the number computed in current i-th round
                if j >= coins[i]:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i]] + 1)  # Use i-th coin
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

#======== <Solution 5> ========#
        # Reference: https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
        coins.sort()
        dp = [0] + [float('inf')] * amount  # dp[i] is the minimum number of coins to make up amount i
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                else:
                    break
        return dp[-1] if dp[-1] != float('inf') else -1
