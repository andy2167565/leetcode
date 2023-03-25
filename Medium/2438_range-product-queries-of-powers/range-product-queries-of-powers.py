class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        s = bin(n)[:1:-1]  # Reverse the binary string to the same non-decreasing order as powers
        powers = [i for i, digit in enumerate(s) if digit == '1']  # Store the exponents of all powers of 2
        return [pow(2, sum(powers[l:r+1]), 10**9 + 7) for l, r in queries]
