class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        # Reference: https://leetcode.com/problems/count-number-of-texts/solutions/2017810/python-o-n-dp-easy-to-understand-with-explanation/
        dp = [1] + [0] * len(pressedKeys)  # dp[i]: The possible combinations of text for first i keys
        for i in range(1, len(pressedKeys) + 1):
            dp[i] = dp[i - 1]  # Consider the last key separately
            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:  # The two last keys are the same
                dp[i] += dp[i - 2]
                if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 3]:  # The three last keys are the same
                    dp[i] += dp[i - 3]
                    if pressedKeys[i - 1] in '79' and i >= 4 and pressedKeys[i - 1] == pressedKeys[i - 4]:  # The four last keys are all 7 or 9
                        dp[i] += dp[i - 4]
            dp[i] %= (10**9 + 7)
        return dp[-1]
