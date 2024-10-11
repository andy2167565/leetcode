class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(stones.count, jewels))
