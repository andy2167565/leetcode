class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        curr, ans = '', 1
        for c in s:
            if int(c) > k:
                return -1
            curr += c
            if int(curr) > k:
                curr = c
                ans += 1
        return ans
