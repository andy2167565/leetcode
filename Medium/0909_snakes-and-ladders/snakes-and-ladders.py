class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, moves, bfs = len(board), {1: 0}, [1]
        for curr in bfs:
            for i in range(curr + 1, curr + 7):
                row, col = divmod(i - 1, n)
                nxt = board[~row][col if not row % 2 else ~col]
                if nxt > 0:
                    i = nxt
                if i == n**2:
                    return moves[curr] + 1
                if i not in moves:
                    moves[i] = moves[curr] + 1
                    bfs.append(i)
        return -1
