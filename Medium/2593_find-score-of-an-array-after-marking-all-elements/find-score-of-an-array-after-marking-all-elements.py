class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans, seen = 0, [0] * (len(nums) + 1)  # Add one more element for edge cases i.e. i = 0 and i = len(nums) - 1
        for num, i in sorted((num, i) for i, num in enumerate(nums)):
            if not seen[i]:
                ans += num
                seen[i] = seen[i - 1] = seen[i + 1] = 1
        return ans
