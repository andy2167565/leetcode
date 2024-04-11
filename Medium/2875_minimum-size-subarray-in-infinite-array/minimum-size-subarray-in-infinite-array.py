class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/solutions/4112000/java-c-python-dp-prefix-sum/
        k, target = divmod(target, sum(nums))
        if not target:
            return k * len(nums)
        res, curr_sum, dp = float('inf'), 0, {0: -1}  # dp[i]: The ending index of prefix sum i
        for i, num in enumerate(nums + nums):
            curr_sum += num
            if curr_sum - target in dp:
                res = min(res, i - dp.get(curr_sum - target))
            dp[curr_sum] = i
        return res + k * len(nums) if res < float('inf') else -1
