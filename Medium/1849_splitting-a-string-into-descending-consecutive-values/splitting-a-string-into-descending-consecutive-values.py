class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i, prev, split):
            if i == len(s) and split > 1:  # Reach the end with more than 1 split
                return True
            l = 1  # Length of current substring
            while i + l <= len(s):
                curr = int(s[i:i + l])
                l += 1
                if prev == -1 or curr == prev - 1:  # First round or the two substrings are in descending order
                    if dfs(i + l - 1, curr, split + 1):
                        return True
            return False
        return dfs(0, -1, 0)
