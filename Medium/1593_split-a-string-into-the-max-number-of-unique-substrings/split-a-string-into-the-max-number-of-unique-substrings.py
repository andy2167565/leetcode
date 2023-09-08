class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtracking(i, seen=set()):
            ans = 0
            if i < len(s):
                for j in range(i + 1, len(s) + 1):
                    if (substring := s[i:j]) not in seen:
                        seen.add(substring)
                        ans = max(ans, backtracking(j, seen) + 1)
                        seen.remove(substring)
            return ans
        return backtracking(0)
