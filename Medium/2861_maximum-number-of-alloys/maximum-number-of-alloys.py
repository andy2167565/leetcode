class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        # Reference: https://leetcode.com/problems/maximum-number-of-alloys/solutions/4061435/python-3-7-lines-bisect-left-w-explanation-t-s-81-97/
        import bisect

        def helper(x):
            return all(sum(max(0, cp * x - st) * co for cp, st, co in zip(comp, stock, cost)) > budget for comp in composition)

        return bisect.bisect_left(range(min(stock) + budget + 1), True, key=helper) - 1
