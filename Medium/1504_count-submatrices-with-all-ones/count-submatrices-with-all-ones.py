class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/count-submatrices-with-all-ones/solutions/2295231/python3-o-mmn-solution-with-a-thought-process/
        m, n, ans = len(mat), len(mat[0]), 0
        for row in range(m):
            col_all_1 = [1] * n
            for sub_row in range(row, m):  # For each subrange of rows, do a sweep from left to right
                subtotal = 0
                for col in range(n):
                    if col_all_1[col] and mat[sub_row][col]:  # Accumulate the number of valid blocks
                        subtotal += 1
                        ans += subtotal
                    else:  # Whenever a column becomes invalid, restart the accumulation
                        col_all_1[col] = subtotal = 0
        return ans
