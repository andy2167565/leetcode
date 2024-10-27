class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        shift = {'DOWN': n, 'UP': -n, 'RIGHT': 1, 'LEFT': -1}
        return sum(map(lambda x: shift[x], commands))
