class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        return ['none', 'equilateral', 'isosceles', 'scalene'][len(set(nums)) * (sum(nums[:2]) > nums[-1])]
