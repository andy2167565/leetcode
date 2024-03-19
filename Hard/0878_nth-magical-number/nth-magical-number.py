class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # Reference: https://leetcode.com/problems/nth-magical-number/solutions/154613/c-java-python-binary-search/
        gcd, remainder = a, b
        while remainder:
            gcd, remainder = remainder, gcd % remainder
        l, r, lcm = 2, 10**14, a * b // gcd
        while l < r:
            mid = (l + r) // 2
            if mid // a + mid // b - mid // lcm < n:
                l = mid + 1
            else:
                r = mid
        return l % (10**9 + 7)
