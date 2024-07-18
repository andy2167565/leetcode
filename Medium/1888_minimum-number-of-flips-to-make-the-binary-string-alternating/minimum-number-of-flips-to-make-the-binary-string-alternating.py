class Solution:
    def minFlips(self, s: str) -> int:
        import collections
        even, odd = collections.Counter(s[0::2]), collections.Counter(s[1::2])  # Count the number of ones and zeros at even and odd positions respectively

        def minOps(even, odd):
            return min(even['0'] + odd['1'], even['1'] + odd['0'])  # min(ones for even and zeros for odd, zeros for even and ones for odd)

        ans = minOps(even, odd)
        if len(s) % 2:  # Only need to do the first operation if s has odd number of digits
            for i, c in enumerate(s):
                even, odd = odd, even  # even and odd are reversed after the first operation
                even[c] += 1
                odd[c] -= 1
                ans = min(ans, minOps(even, odd))  # Update the minimum number of flips
        return ans
