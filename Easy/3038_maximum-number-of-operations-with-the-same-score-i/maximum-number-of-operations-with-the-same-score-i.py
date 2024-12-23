class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans, score = 1, sum(nums[:2])
        for i in range(3, len(nums), 2):
            if nums[i - 1] + nums[i] != score:
                break
            ans += 1
        return ans
