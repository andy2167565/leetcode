class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m, n = max(nums), min(nums)
        for i in (range(m, 0, -1)):
            if not m % i and not n % i:
                return i
