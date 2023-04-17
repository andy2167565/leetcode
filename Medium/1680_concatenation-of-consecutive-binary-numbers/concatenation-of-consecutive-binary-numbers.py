class Solution:
    def concatenatedBinary(self, n: int) -> int:
#======== <Solution 1> ========#
        ans, mod = '', 10**9 + 7
        for i in range(1, n + 1):
            ans += bin(i)[2:]
        return int(ans, 2) % mod

#======== <Solution 2> ========#
        ans, bit_len, mod = 0, 0, 10**9 + 7
        for i in range(1, n + 1):
            bit_len += not i & (i - 1)  # Add 1 more space for the carry if i is power of 2 or 1 (i == 0 after removing the rightmost bit "1")
            ans = (ans << bit_len | i) % mod
        return ans

#======== <Solution 3> ========#
        ans, mod = 0, 10**9 + 7
        for i in range(1, n + 1):
            ans = (ans << i.bit_length() | i) % mod
        return ans

#======== <Solution 4> ========#
        import functools
        return functools.reduce(lambda ans, i: (ans << i.bit_length() | i) % (10**9 + 7), range(1, n + 1))
