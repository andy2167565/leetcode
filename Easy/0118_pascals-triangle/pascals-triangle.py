class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
#======== <Solution 1> ========#
        ans = [[1]]
        for row_num in range(1, numRows):
            # First number of each row is 1
            row = [1]
            for j in range(1, row_num):
                # row_num - 1: Iterate numbers in previous row
                # Add sequential pair of numbers
                row.append(ans[row_num - 1][j - 1] + ans[row_num - 1][j])
            # Last number of each row is also 1
            row.append(1)
            ans.append(row)
        return ans

#======== <Solution 2> ========#
        # Create a triangle of all ones
        ans = [[1] * (row_num + 1) for row_num in range(numRows)]
        for row_num in range(2, numRows):
            for j in range(1, row_num):
                # Replace elements in the middle with sum of elements
                # above-and-to-the-left and above-and-to-the-right
                ans[row_num][j] = ans[row_num - 1][j - 1] + ans[row_num - 1][j]
        return ans

#======== <Solution 3: Combinations> ========#
        # Each entry can be calculated by combinations formula
        import math
        C = lambda n, r: math.factorial(n) // math.factorial(r) // math.factorial(n - r)
        return [[C(n, r) for r in range(n + 1)] for n in range(numRows)]

#======== <Solution 4> ========#
        ans = [[1]]
        for _ in range(numRows - 1):
            ans.append([a + b for a, b in zip([0] + ans[-1], ans[-1] + [0])])
        return ans
