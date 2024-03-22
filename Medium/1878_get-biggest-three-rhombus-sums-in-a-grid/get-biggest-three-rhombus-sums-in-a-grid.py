class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/solutions/1238637/python-3-brute-force-greedy/
        import heapq
        m, n, seen = len(grid), len(grid[0]), {cell for row in grid for cell in row}
        heap = list(seen)
        heapq.heapify(heap)
        while len(heap) > 3:
            heapq.heappop(heap)
        for i in range(1, m):
            for j in range(1, n):
                for k in range(1, min(i, m - 1 - i, j, n - 1 - j) + 1):  # Half of the diagonal
                    curr = 0
                    for l in range(1, k + 1):  # The difference of y-axis between the center and the cell on the border
                        curr += grid[i - k + l][j + l] + grid[i + l][j + k - l] + grid[i + k - l][j - l] + grid[i - l][j - k + l]
                    if curr not in seen:
                        seen.add(curr)
                        heapq.heappush(heap, curr)
                        if len(heap) > 3:
                            heapq.heappop(heap)
        return sorted(heap, reverse=True)
