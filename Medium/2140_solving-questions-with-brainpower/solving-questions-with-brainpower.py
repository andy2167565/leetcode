class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import functools
        @functools.cache
        def dfs(i):
            return 0 if i >= len(questions) else max(dfs(i + 1), questions[i][0] + dfs(i + 1 + questions[i][1]))
        return dfs(0)

#======== <Solution 2> ========#
        dp = [0] * (len(questions) + 1)  # dp[i]: Maximum points we can get starting from index i
        for i in range(len(questions) - 1, -1, -1):
            points, brainpower = questions[i]
            dp[i] = max(dp[i + 1], points + dp[min(i + 1 + brainpower, len(questions))])
        return dp[0]
