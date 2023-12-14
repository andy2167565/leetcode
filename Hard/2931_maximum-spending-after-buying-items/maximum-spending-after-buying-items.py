class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        return sum((d + 1) * v for d, v in enumerate(sorted(val for row in values for val in row)))
