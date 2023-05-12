class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # If we have a zero anywhere we can use it to flip all negatives into positives.
        # If we have even number of negatives, we can turn all negatives into positives.
        # Otherwise, we turn the smallest absolute value into a negative, and everything else into positives.
        abs_total = odd_neg = 0
        min_abs = float('inf')
        for row in matrix:
            for num in row:
                abs_total += abs(num)
                min_abs = min(min_abs, abs(num))
                if num < 0:
                    odd_neg ^= 1
        return abs_total - 2 * min_abs * odd_neg
