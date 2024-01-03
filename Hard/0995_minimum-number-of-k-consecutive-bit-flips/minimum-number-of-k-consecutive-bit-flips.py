class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/solutions/238609/java-c-python-one-pass-and-o-1-space/
        ans = curr = 0  # The number of flips in the current sliding window of size k
        for i in range(len(nums)):
            if i >= k and nums[i - k] == 2:  # nums[i - k] is flipped and out of the sliding window
                curr -= 1
            if curr % 2 == nums[i]:  # Need to flip
                if i + k > len(nums):
                    return -1
                nums[i] = 2  # Marked as flipped
                curr, ans = curr + 1, ans + 1
        return ans
