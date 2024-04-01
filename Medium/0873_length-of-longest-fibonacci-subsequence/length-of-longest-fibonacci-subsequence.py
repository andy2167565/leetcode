class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
# Reference: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/solutions/152343/c-java-python-check-pair/
#======== <Solution 1> ========#
        import itertools
        s, ans = set(arr), 2
        for a, b in itertools.combinations(arr, 2):
            l = 2
            while a + b in s:
                a, b, l = b, a + b, l + 1
            ans = max(ans, l)
        return ans if ans > 2 else 0

#======== <Solution 2> ========#
        import collections, itertools
        s, dp = set(arr), collections.defaultdict(int)  # dp[a, b]: The length of Fibonacci sequence that ends up with (a, b)
        for a, b in itertools.combinations(arr, 2):
            if b - a < a and b - a in s:
                dp[a, b] = dp.get((b - a, a), 2) + 1
        return max(dp.values(), default=0)
