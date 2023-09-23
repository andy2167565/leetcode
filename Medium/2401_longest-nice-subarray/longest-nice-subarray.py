class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = window = i = 0
        for j in range(len(nums)):
            while window & nums[j]:  # nums[j] has duplicate set bits for current sliding window
                window ^= nums[i]  # Remove the leftmost element out of the window
                i += 1  # Shrink left bound of current sliding window
            window |= nums[j]  # Add nums[j] into the window for later comparison
            ans = max(ans, j - i + 1)
        return ans
