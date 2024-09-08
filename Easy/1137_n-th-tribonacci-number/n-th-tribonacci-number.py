class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0, 1, 1]
        for i in range(3, n + 1):
            tribonacci[i % 3] = sum(tribonacci)
        return tribonacci[n % 3]
