class Solution:
    def monkeyMove(self, n: int) -> int:
        # Reference: https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/solutions/3111664/java-c-python-fast-pow/
        mod = 10 ** 9 + 7
        return (pow(2, n, mod) - 2) % mod
