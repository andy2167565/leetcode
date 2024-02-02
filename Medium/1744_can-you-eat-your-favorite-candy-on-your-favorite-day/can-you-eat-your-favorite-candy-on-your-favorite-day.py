class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # Reference: https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/solutions/1042983/python-prifix-sum/
        import itertools
        prefix_sums = list(itertools.accumulate(candiesCount, initial=0))
        return [prefix_sums[t] // c <= d < prefix_sums[t + 1] for t, d, c in queries]
