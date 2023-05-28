class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#======== <Solution 1> ========#
        import functools
        @functools.cache
        def dfs(i, extra):
            if i >= len(s):
                return extra
            min_extra = dfs(i + 1, extra)  # Base case, just move on to the next character
            for word in dictionary:
                if s[i:].startswith(word):  # word starts at current index
                    min_extra = min(min_extra, dfs(i + len(word), extra - len(word)))  # Remove word from extra and keep searching
            return min_extra
        return dfs(0, len(s))

#======== <Solution 2> ========#
        n = len(s)
        dp = [n] * (n + 1)  # dp[i]: Number of extra characters while looking up substrings of s[:i] in dictionary
        for i in range(1, n + 1):
            for word in dictionary:
                if i >= len(word) and s[i - len(word):i] == word:
                    dp[i] = min(dp[i], dp[i - len(word)] - len(word))
            dp[i] = min(dp[i], dp[i - 1])
        return dp[n]
