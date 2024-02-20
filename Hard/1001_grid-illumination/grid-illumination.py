class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/grid-illumination/solutions/242991/python-clean-short-code/
        import collections
        lamps = {(r, c) for r, c in lamps}
        row, col, diag, andi = collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int)
        for r, c in lamps:
            row[r] += 1
            col[c] += 1
            diag[r - c] += 1
            andi[r + c] += 1
        ans = []
        for r, c in queries:
            ans.append(int(row[r] + col[c] + diag[r - c] + andi[r + c] > 0))
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i, j) in lamps:
                        lamps.remove((i, j))
                        row[i] -= 1
                        col[j] -= 1
                        diag[i - j] -= 1
                        andi[i + j] -= 1
        return ans
