class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        import collections
        return max(collections.Counter(tuple(num ^ row[0] for num in row) for row in matrix).values())
