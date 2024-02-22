class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Reference: https://leetcode.com/problems/smallest-integer-divisible-by-k/solutions/260852/java-c-python-o-1-space-with-proves-of-pigeon-holes/
        if not k % 2 or not k % 5:
            return -1
        r = 0
        for num in range(1, k + 1):
            r = (r * 10 + 1) % k
            if not r:
                return num
