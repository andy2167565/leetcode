class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps, seat = 0, {num: i for i, num in enumerate(row)}
        for i, person in enumerate(row):
            j = seat[person + (1 if not person % 2 else -1)]  # The spouse's seat
            if abs(i - j) > 1:  # A swap is required
                row[i + 1], row[j] = row[j], row[i + 1]
                seat[row[i + 1]], seat[row[j]] = i + 1, j
                swaps += 1
        return swaps
