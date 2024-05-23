class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        res = 1
        for i in range(1, numPeople // 2 + 1):
            res *= numPeople - i + 1
            res //= i
        return res // (numPeople // 2 + 1) % (10**9 + 7)
