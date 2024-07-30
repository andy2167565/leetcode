class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        import functools, collections

        @functools.cache
        def dfs(left):
            if left == len(nums):  # Reached the end of nums
                return 0
            importance_value, ans, counter = k, float('inf'), collections.defaultdict(int)
            for right, num in enumerate(nums[left:], start=left):
                counter[num] += 1
                importance_value += (counter[num] > 1) + (counter[num] == 2)  # Either a pair exists or add the extra number
                ans = min(ans, importance_value + dfs(right + 1))
            return ans

        return dfs(0)
