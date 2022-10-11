class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#======== <Solution 1>: Dynamic Programming - Bottom-up ========#
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])

#======== <Solution 2>: Dynamic Programming - Top-down ========#
        # Reference: https://leetcode.com/problems/min-cost-climbing-stairs/discuss/1256642/JS-Python-Java-C%2B%2B-or-Simple-DP-Solution-w-Explanation
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

#======== <Solution 3>: Dynamic Programming - Top-down with Memoization ========#
        # Reference: https://leetcode.com/problems/min-cost-climbing-stairs/discuss/110111/The-ART-of-dynamic-programming
        @cache
        def helper(i):
            if i >= len(cost): return 0  # Base case: reached the top floor
            return cost[i] + min(helper(i + 1), helper(i + 2))  # Recursive case: cost of i-th step + min(one step, two steps)
        return min(helper(0), helper(1))  # Minimal cost starting at first or second step
