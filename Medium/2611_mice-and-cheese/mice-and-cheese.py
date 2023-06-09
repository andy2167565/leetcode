class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        import heapq
        return sum(reward2) + sum(heapq.nlargest(k, (r1 - r2 for r1, r2 in zip(reward1, reward2))))
