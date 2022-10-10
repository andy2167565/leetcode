class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
#======== <Solution 1> ========#
        ans = [1]
        for row_num in range(1, rowIndex + 1):
            row = [1]
            for j in range(1, row_num):
                row.append(ans[j - 1] + ans[j])
            row.append(1)
            ans = row
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/pascals-triangle-ii/discuss/38574/Simple-Python-5-lines-36ms
        ans = [1] * (rowIndex + 1)
        for row_num in range(2, rowIndex + 1):
            for j in range(row_num - 1, 0, -1):
                ans[j] += ans[j - 1]
        return ans

#======== <Solution 3: Combinations> ========#
        import math
        C = lambda n, r: math.factorial(n) // math.factorial(r) // math.factorial(n - r)
        return [C(rowIndex, r) for r in range(rowIndex + 1)]

#======== <Solution 4> ========#
        ans = [1]
        for _ in range(rowIndex):
            ans = [a + b for a, b in zip([0] + ans, ans + [0])]
        return ans
