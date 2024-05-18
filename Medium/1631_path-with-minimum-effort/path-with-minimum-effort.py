class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0
        minHeap = [(0, 0, 0)]
        while minHeap:
            effort, row, col = heappop(minHeap)
            if effort > efforts[row][col]:  # Skip the outdated version
                continue
            if (row, col) == (m - 1, n - 1):  # Reach the bottom-right cell
                return effort
            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                nrow, ncol = row + dr, col + dc
                if 0 <= nrow < m and 0 <= ncol < n:
                    new_effort = max(effort, abs(heights[nrow][ncol] - heights[row][col]))
                    if efforts[nrow][ncol] > new_effort:
                        efforts[nrow][ncol] = new_effort
                        heappush(minHeap, (efforts[nrow][ncol], nrow, ncol))
