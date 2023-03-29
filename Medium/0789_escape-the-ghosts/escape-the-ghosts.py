class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return all(abs(target[0]) + abs(target[1]) < abs(target[0] - x) + abs(target[1] - y) for x, y in ghosts)
