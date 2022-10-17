class Solution:
    def numDecodings(self, s: str) -> int:
# This problem is a variation of 70. Climing Stairs: https://leetcode.com/problems/climbing-stairs/
# Reference: https://leetcode.com/problems/decode-ways/discuss/1410794/C%2B%2BPython-From-Top-down-DP-to-Bottom-up-DP-O(1)-Space-Clean-and-Concise
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)
        @cache
        def dfs(i):
            if i == len(s): return 1
            if s[i] == '0': return 0
            return dfs(i + 1) + (dfs(i + 2) if 10 <= int(s[i: i + 2]) <= 26 else 0)
        return dfs(0)

#======== <Solution 2> ========#
        if s[0] == '0': return 0
        dp = [1, 1] + [0] * (len(s) - 1)
        for i in range(2, len(s) + 1):
            if int(s[i - 1]):  # One step jump
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:  # Two step jump
                dp[i] += dp[i - 2]
        return dp[-1]

#======== <Solution 3> ========#
        if s[0] == '0': return 0
        prev = curr = 1
        for i in range(1, len(s)):
            count = 0
            if s[i] != '0':  # 1 ~ 9
                count += curr
            if s[i - 1] == '1' or (s[i - 1] == '2' and int(s[i]) < 7):  # 10 ~ 26
                count += prev
            prev, curr = curr, count
        return curr
