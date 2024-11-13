class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for j, col in enumerate(zip(*matrix)):
            for i, num in enumerate(col):
                if num == -1:
                    matrix[i][j] = max(col)
        return matrix
