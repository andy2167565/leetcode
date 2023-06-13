class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        import math
        M, Mx, My = float('-inf'), 0, 0
        for i in range(51):
            for j in range(51):
                sq = 0
                for x, y, q in towers:
                    d = math.dist((x, y), (i, j))
                    if d <= radius:
                        sq += int(q / (1 + d))
                if sq > M:
                    M, Mx, My = sq, i, j
        return [Mx, My]
