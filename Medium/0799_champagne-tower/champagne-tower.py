class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr_row, curr_level = 0, [poured]
        while any(curr_level):
            if curr_row == query_row:
                return min(curr_level[query_glass], 1)
            next_level = [0] * (len(curr_level) + 1)
            for i, cup in enumerate(curr_level):
                if (left := cup - 1) > 0:  # The remaining cups fall equally to the left and right of glasses in next row
                    next_level[i] += left / 2
                    next_level[i + 1] += left / 2
            curr_row += 1
            curr_level = next_level
        return 0
