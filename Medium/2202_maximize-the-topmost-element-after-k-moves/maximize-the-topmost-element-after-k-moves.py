class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1 if k & 1 else nums[0]
        ans = max(nums[:min(len(nums), k - 1)]) if k > 1 else -1  # Add back a removed element
        return max(ans, nums[k]) if k < len(nums) else ans  # Remove all k topmost elements
