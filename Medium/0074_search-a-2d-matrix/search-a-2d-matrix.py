class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#======== <Solution 1> ========#
        return any(target in row for row in matrix)

#======== <Solution 2> ========#
        for row in matrix:
            if row[-1] >= target:
                return target in row
        return False

#======== <Solution 3> ========#
        n = len(matrix[0])
        lo, hi = 0, len(matrix) * n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            num = matrix[mid // n][mid % n]
            if num < target:
                lo = mid + 1
            else:
                hi = mid
        return matrix[lo // n][lo % n] == target

#======== <Solution 4> ========#
        import bisect
        r = bisect.bisect_left(matrix, target, key=lambda row: row[-1])  # Find the candidate row
        return r < len(matrix) and matrix[r][bisect.bisect_left(matrix[r], target)] == target  # Find the candidate cell in that row
