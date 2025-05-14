class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        import itertools
        return list(itertools.accumulate(cost, min))
