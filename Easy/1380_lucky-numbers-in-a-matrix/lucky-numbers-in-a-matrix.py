class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return [max(col) for col in zip(*matrix) if max(col) in map(min, matrix)]
