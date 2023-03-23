class Solution:
    def countHousePlacements(self, n: int) -> int:
        prev = curr = 1
        for _ in range(n):
            prev, curr = curr, prev + curr
        return (curr * curr) % (10**9 + 7)
