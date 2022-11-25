class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
        dp = [False] * len(s)  # dp[i] is True if s[:i + 1] can be segmented into a space-separated sequence of one or more dictionary words
        for i in range(len(s)):
            for w in wordDict:
                # Current word starts at index i AND (a word ends before index i OR current word starts from the beginning of the string)
                if w == s[i: i + len(w)] and (dp[i - 1] or not i):
                    dp[i + len(w) - 1] = True
        return dp[-1]

#======== <Solution 2> ========#
        dp = [True] + [False] * len(s)  # dp[i] is True if s[:i] can be segmented into a space-separated sequence of one or more dictionary words
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] |= dp[i - len(word)]
        return dp[-1]

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python
        dp = [True]  # dp[i] is True if s[:i] can be segmented into a space-separated sequence of one or more dictionary words
        for end in range(1, len(s) + 1):
            dp += any(dp[start] and s[start:end] in wordDict for start in range(end)),
        return dp[-1]

# Reference: https://leetcode.com/problems/word-break/discuss/1455100/Python-3-solutions%3A-Top-down-DP-Bottom-up-DP-then-Optimised-with-Trie-Clean-and-Concise
#======== <Solution 4> ========#
        @cache
        def dp(start):  # dp(i) is True if s[i:] can be segmented into a space-separated sequence of one or more dictionary words
            if start == len(s):  # Found a valid way to break words
                return True
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict and dp(end):
                    return True
            return False
        return dp(0)

#======== <Solution 5> ========#
        dp = [False] * len(s) + [True]  # dp[i] is True if s[i:] can be segmented into a space-separated sequence of one or more dictionary words
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
                    break
        return dp[0]

#======== <Solution 6> ========#
        # Reference: https://leetcode.com/problems/word-break/discuss/428606/Python-Simple-Iterative-BFS-or-DFS-24ms
        import collections
        q, seen = collections.deque([s]), set()
        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    rest = s[len(word):]
                    if not rest:
                        return True
                    if rest not in seen:
                        q.append(rest)
                        seen.add(rest)
        return False
