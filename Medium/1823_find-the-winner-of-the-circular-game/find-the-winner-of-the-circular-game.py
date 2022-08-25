class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
#======== <Solution 1> ========#
        players, count = list(range(1, n + 1)), 0
        while len(players) > 1:
            count = (count + k - 1) % len(players)
            del players[count]
        return players[0]

#======== <Solution 2> ========#
        from collections import deque
        players = deque([i for i in range(1, n + 1)])
        while len(players) > 1:
            players.rotate(-k)
            players.pop()
        return players.pop()

# Reference: https://en.wikipedia.org/wiki/Josephus_problem
#======== <Solution 3> ========#
        # Josephus Problem Recurrence - Recursive
        return 1 if n == 1 else (self.findTheWinner(n - 1, k) + k - 1) % n + 1

#======== <Solution 4> ========#
        # Josephus Problem Recurrence Simpler Form  - Recursive
        return self.josephus(n, k) + 1
    def josephus(self, n: int, k: int) -> int:
        return 0 if n == 1 else (self.josephus(n - 1, k) + k) % n

#======== <Solution 5> ========#
        # Josephus Problem Recurrence Simpler Form  - Iterative
        winner = 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1
