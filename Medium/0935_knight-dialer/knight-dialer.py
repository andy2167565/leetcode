class Solution:
    def knightDialer(self, n: int) -> int:
        directions = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        curr_counts = [1] * 10
        for _ in range(n - 1):
            next_counts = [0] * 10
            for src_key in range(10):
                for dst_key in directions[src_key]:
                    next_counts[dst_key] += curr_counts[src_key]
            curr_counts = next_counts
        return sum(curr_counts) % (10 ** 9 + 7)
