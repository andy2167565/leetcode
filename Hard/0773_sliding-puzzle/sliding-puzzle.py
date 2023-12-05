class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        import collections
        neighbors = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        state = (*board[0], *board[1])
        queue, seen, moves = collections.deque([state]), {state}, 0
        while queue:
            for _ in range(len(queue)):
                state = list(queue.popleft())
                i = state.index(0)
                if state == [1, 2, 3, 4, 5, 0]:
                    return moves
                for j in neighbors[i]:
                    curr = state[:]
                    curr[i], curr[j] = curr[j], 0
                    curr = tuple(curr)
                    if curr not in seen:
                        queue.append(curr)
                        seen.add(curr)
            moves += 1
        return -1
