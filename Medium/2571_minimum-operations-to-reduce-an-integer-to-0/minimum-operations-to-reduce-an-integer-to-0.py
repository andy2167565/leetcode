class Solution:
    def minOperations(self, n: int) -> int:
#======== <Solution 1> ========#
        # Reference 1: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3204095/easiest-solution-better-than-the-most-voted-one-explained/
        # Reference 2: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3203727/python-easy-solution-beats-100/
        import math
        ans = 0
        while n:
            exp = int(math.log2(n))
            n = min(n - 2**exp, 2**(exp + 1) - n)
            ans += 1
        return ans

# Reference: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3203994/java-c-python-1-line-solution/
#======== <Solution 2> ========#
        ans = 0
        while n:
            if not n % 2:  # n is even
                n >>= 1  # Keep reducing the bits until we hit bit 1 at the end
            elif n & 2:  # Continuous bit 1's at the end, e.g. 100111
                n += 1  # Add 1 to n to make the continuous 1's a power of 2
                ans += 1
            else:  # Single bit 1 at the end, e.g. 101
                n >>= 1  # Subtract a power of 2 from n
                ans += 1
        return ans

#======== <Solution 3> ========#
        return (n ^ (n * 3)).bit_count()
