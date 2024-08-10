class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0] * (1 + max(ages))  # dp[i]: The highest score achieved by the team with players under age i without conflicts
        for score, age in sorted(zip(scores, ages)):
            dp[age] = score + max(dp[:age + 1])
        return max(dp)
