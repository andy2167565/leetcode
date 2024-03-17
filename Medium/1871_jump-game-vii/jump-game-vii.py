class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Reference: https://leetcode.com/problems/jump-game-vii/solutions/1224804/java-c-python-one-pass-dp/
        dp = [c == '0' for c in s]  # dp[i] is True if we can reach s[i]
        prev = 0  # The number of previous positions that we can jump from
        for i in range(1, len(s)):
            if i >= minJump:
                prev += dp[i - minJump]
            if i > maxJump:
                prev -= dp[i - maxJump - 1]
            dp[i] &= prev > 0
        return dp[-1]
