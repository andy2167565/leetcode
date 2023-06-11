class Solution:
    def isFascinating(self, n: int) -> bool:
#======== <Solution 1> ========#
        s = str(n) + str(2 * n) + str(3 * n)
        return len(s) == len(set(s)) == 9 and '0' not in s

#======== <Solution 2> ========#
        return ''.join(sorted(str(n) + str(2 * n) + str(3 * n))) == '123456789'

#======== <Solution 3> ========#
        return n in {192, 219, 273, 327}  # n is fascinating only if 123 <= n <= 329, and n must be cyclic permutations of the digits of 192 or 273
