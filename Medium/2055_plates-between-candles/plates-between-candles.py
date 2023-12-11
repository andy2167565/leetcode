class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/plates-between-candles/solutions/1549018/java-c-python-binary-search-and-o-q-n-solution/
        import bisect
        ans, candles = [], [i for i, c in enumerate(s) if c == '|']
        for l, r in queries:
            i = bisect.bisect_left(candles, l)
            j = bisect.bisect(candles, r) - 1
            ans.append((candles[j] - candles[i]) - (j - i) if i < j else 0)
        return ans
