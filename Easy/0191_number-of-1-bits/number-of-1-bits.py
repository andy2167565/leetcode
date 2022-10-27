class Solution:
    def hammingWeight(self, n: int) -> int:
#======== <Solution 1> ========#
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans

#======== <Solution 2> ========#
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans

#======== <Solution 3> ========#
        return bin(n).count('1')

#======== <Solution 4> ========#
        import collections
        return collections.Counter(bin(n)).get('1', 0)
