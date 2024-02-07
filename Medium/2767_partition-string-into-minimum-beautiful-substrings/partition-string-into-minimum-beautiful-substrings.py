class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        bins = [bin(5**i)[2:] for i in range(7)]
        def dfs(s):
            if not s.replace('_', ''):  # s can be partitioned into beautiful substrings
                self.ans = min(self.ans, len(s))
            for num in bins:
                if num in s:
                    dfs(s.replace(num, '_'))  # Mark all occurrences of num in s

        self.ans = float('inf')
        dfs(s)
        return -1 if self.ans == float('inf') else self.ans
