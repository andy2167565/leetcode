class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        return len(set(num for start, end in nums for num in range(start, end + 1)))
