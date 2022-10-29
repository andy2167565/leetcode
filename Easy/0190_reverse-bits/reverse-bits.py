class Solution:
    def reverseBits(self, n: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/reverse-bits/discuss/732138/Python-O(32)-simple-solution-explained
        ans = 0
        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans

#======== <Solution 2> ========#
        return int(bin(n)[2:].zfill(32)[::-1], 2)
