class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/solutions/1403913/python-math-oneliner-with-proof-explained/
        return (pow(2**p - 2, 2**(p - 1) - 1, 10**9 + 7) * (2**p - 1)) % (10**9 + 7)
