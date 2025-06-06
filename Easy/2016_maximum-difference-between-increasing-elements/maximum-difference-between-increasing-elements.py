class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans, minNum = -1, nums[0]
        for num in nums:
            ans = max(ans, num - minNum)
            minNum = min(minNum, num)
        return ans or -1
