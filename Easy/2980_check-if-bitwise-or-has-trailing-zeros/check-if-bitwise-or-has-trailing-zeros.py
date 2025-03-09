class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = 0
        for num in nums:
            if not num % 2:
                even += 1
            if even == 2:
                return True
        return False
