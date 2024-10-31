class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import bisect
        stones.sort()
        while len(stones) > 1:
            bisect.insort(stones, stones.pop() - stones.pop())
        return stones[0]
