class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # Reference: https://leetcode.com/problems/visit-array-positions-to-maximize-score/solutions/3801776/java-c-python-dp-solution/
        dp = [-x, -x]  # Maximum scores with last visits even and odd respectively
        dp[nums[0] & 1] = nums[0]
        for num in nums[1:]:
            dp[num & 1] = max(dp[num & 1], dp[num & 1 ^ 1] - x) + num
        return max(dp)
