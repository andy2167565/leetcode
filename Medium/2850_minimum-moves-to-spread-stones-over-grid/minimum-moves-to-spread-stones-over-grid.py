class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/solutions/4028356/python-3-6-lines-permutation-w-explanation-t-s-65-71/
        import itertools

        def dist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        zeros, spare = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    zeros.append((i, j))
                if grid[i][j] > 1:
                    spare.extend([(i, j)] * (grid[i][j] - 1))
        return min(sum(map(dist, zeros, perm)) for perm in set(itertools.permutations(spare)))
