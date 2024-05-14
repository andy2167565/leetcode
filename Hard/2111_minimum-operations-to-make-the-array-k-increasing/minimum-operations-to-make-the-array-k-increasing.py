class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/solutions/1634978/python-short-lis-explained/
        import bisect

        def LIS(nums):
            dp = [float('inf')] * (len(nums) + 1)
            for num in nums:
                dp[bisect.bisect(dp, num)] = num
            return dp.index(float('inf'))

        ans = 0
        for i in range(k):
            nums = arr[i::k]
            ans += len(nums) - LIS(nums)
        return ans
