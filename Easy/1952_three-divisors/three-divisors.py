class Solution:
    def isThree(self, n: int) -> bool:
        return sum(not n % i for i in range(1, n + 1)) == 3
