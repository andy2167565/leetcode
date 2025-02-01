class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = count = 0
        for c in s:
            count += 1 if c == 'L' else -1
            if not count:
                ans += 1
        return ans
