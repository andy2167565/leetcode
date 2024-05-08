class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/solutions/2588015/java-c-python-bit-solution-with-explanation/
        n = len(nums)
        ans, last = [0] * n, [0] * 32  # last[i]: The last occurrence index of bit 1 at bit position i in the binary representation of the numbers
        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            ans[i] = max(1, max(last) - i + 1)
        return ans
