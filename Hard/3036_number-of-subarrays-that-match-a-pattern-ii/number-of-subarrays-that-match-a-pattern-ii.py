class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # Reference: https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/solutions/4708937/python-kmp-solution/
        import itertools
        def prefix(s):
            dp = [0] * len(s)
            for i in range(1, len(s)):
                v = dp[i - 1]
                while v and s[i] != s[v]:
                    v = dp[v - 1]
                dp[i] = v + (s[i] == s[v])
            return dp

        trend = [(x < y) - (x > y) for x, y in itertools.pairwise(nums)]  # Get the pattern of nums
        return prefix(pattern + [2] + trend).count(len(pattern))
