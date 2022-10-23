class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734162/C%2B%2BPython-Binary-Search
        cost_func = lambda x: sum(abs(num - x) * c for num, c in zip(nums, cost))
        left, right = min(nums), max(nums)
        ans = cost_func(left)
        while left < right:
            mid = (left + right) // 2
            left_cost, right_cost = cost_func(mid), cost_func(mid + 1)
            ans = min(left_cost, right_cost)
            if left_cost < right_cost:
                right = mid
            else:
                left = mid + 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734183/Python3-Weighted-Median-O(NlogN)-with-Explanations
        numCost = sorted((num, c) for num, c in zip(nums, cost))
        median, count = (sum(cost) + 1) // 2, 0
        # Find weighted median
        for num, c in numCost:
            count += c
            if count >= median:
                target = num
                break
        return sum(abs(num - target) * c for num, c in numCost)
