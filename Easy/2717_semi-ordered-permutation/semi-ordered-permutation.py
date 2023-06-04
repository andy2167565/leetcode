class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        l, r = nums.index(1), nums.index(len(nums))
        return l + len(nums) - 1 - r - (l > r)
