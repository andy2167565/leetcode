class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        import bisect
        return max(bisect.bisect_left(nums, 0), len(nums) - bisect.bisect_left(nums, 1))
