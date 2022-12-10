class Solution:
    def rob(self, nums: List[int]) -> int:
# Reference: https://leetcode.com/problems/house-robber/solutions/1605797/c-python-4-simple-solutions-w-explanation-optimization-from-brute-force-to-dp/
#======== <Solution 1> ========#
        @cache
        def dfs(i):
            return max(dfs(i + 1), nums[i] + dfs(i + 2)) if i < len(nums) else 0
        return dfs(0)

#======== <Solution 2> ========#
        dp = [nums[0]] + [0] * (len(nums) - 1)
        for i, num in enumerate(nums[1:], 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num)
        return dp[-1]

#======== <Solution 3> ========#
        prev2 = prev = curr = 0
        for num in nums:
            prev2 = prev  # dp[i - 2]
            prev = curr  # dp[i - 1]
            curr = max(prev, prev2 + num)  # dp[i]
        return curr

#======== <Solution 4> ========#
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr
