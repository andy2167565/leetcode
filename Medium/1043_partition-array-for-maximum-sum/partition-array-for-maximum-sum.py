class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/partition-array-for-maximum-sum/solutions/290863/java-c-python-dp-o-k-space/
        dp = [0] * (len(arr) + 1)  # dp[i]: Maximum sum we can get in arr[:i]
        for i in range(1, len(arr) + 1):
            curr_max = 0
            for j in range(1, min(k, i) + 1):  # Change last j numbers separately to the maximum of them
                curr_max = max(curr_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + curr_max * j)
        return dp[-1]
