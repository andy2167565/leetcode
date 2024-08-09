class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Reference: https://leetcode.com/problems/stone-game-iii/solutions/564260/java-c-python-dp-o-1-space/
        dp = [0] * 3  # dp[i]: The highest score that Alice can win over Bob if we ignore stones before stoneValue[i]
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i: i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        return ['Tie', 'Alice', 'Bob'][(dp[0] > 0) - (dp[0] < 0)]
