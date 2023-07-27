class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        import functools
        @functools.cache
        def dfs(i, cost):  # Return sum of subsequence closest to target
            if cost >= target or i == len(toppingCosts):
                return cost
            return min(dfs(i + 1, cost), dfs(i + 1, cost + toppingCosts[i]), key=lambda x: (abs(x - target), x))
        ans = float('inf')
        toppingCosts *= 2
        for cost in baseCosts:
            ans = min(ans, dfs(0, cost), key=lambda x: (abs(x - target), x))
        return ans
