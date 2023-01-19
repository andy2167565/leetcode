class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
# Reference: https://leetcode.com/problems/rotate-image/solutions/18884/seven-short-solutions-1-to-7-lines/
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/rotate-image/solutions/18872/a-common-method-to-rotate-the-image/
        up, down = 0, len(matrix) - 1
        while up < down:  # Reverse up to down
            matrix[up], matrix[down] = matrix[down], matrix[up]
            up += 1
            down -= 1
        for i in range(1, len(matrix)):  # Transpose
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#======== <Solution 2> ========#
        matrix[:] = map(list, zip(*matrix[::-1]))

#======== <Solution 3> ========#
        # Reference 1: https://leetcode.com/problems/rotate-image/solutions/2503184/python-easily-understood-faster-than-99-less-than-99/
        # Reference 2: https://leetcode.com/problems/rotate-image/solutions/1175496/js-python-java-c-easy-4-way-swap-solution-w-explanation/
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - n // 2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
