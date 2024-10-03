class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return int((sum(nums) - sum(set(nums))) // (len(nums) // 2 - 1))
