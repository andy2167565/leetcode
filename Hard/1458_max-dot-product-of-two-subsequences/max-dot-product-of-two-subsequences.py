class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Reference: https://leetcode.com/problems/max-dot-product-of-two-subsequences/solutions/4143612/90-14-dynamic-programming-optimized/
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]  # dp[i][j]: The maximum dot product between the first i elements of nums1 and the first j elements of nums2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], nums1[i - 1] * nums2[j - 1] + max(0, dp[i - 1][j - 1]))
        return dp[m][n]
