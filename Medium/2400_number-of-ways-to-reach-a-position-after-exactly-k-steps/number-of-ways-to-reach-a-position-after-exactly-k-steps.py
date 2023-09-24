class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/solutions/2527381/java-c-python-math-solution-o-klogk/
        import math
        return math.comb(k, (endPos - startPos + k) // 2) % (10**9 + 7) if not (startPos - endPos - k) % 2 else 0
