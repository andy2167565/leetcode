class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/count-substrings-that-differ-by-one-character/discuss/917701/C%2B%2BJavaPython3-O(n-3)-greater-O(n-2)
        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                miss = pos = 0
                while i + pos < len(s) and j + pos < len(t) and miss < 2:
                    miss += s[i + pos] != t[j + pos]
                    ans += miss == 1
                    pos += 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/count-substrings-that-differ-by-one-character/discuss/917985/JavaC%2B%2BPython-Time-O(nm)-Space-O(1)
        def check(i: int, j: int) -> int:
            ans = prev = curr = 0
            for k in range(min(m - i, n - j)):
                curr += 1
                if s[i + k] != t[j + k]:
                    prev, curr = curr, 0
                ans += prev
            return ans
        m, n = len(s), len(t)
        return sum(check(i, 0) for i in range(m)) + sum(check(0, j) for j in range(1, n))
