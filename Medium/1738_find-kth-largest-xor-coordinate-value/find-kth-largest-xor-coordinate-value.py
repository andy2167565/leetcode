class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        minHeap = []
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if i:
                    cell ^= matrix[i - 1][j]
                if j:
                    cell ^= matrix[i][j - 1]
                if i and j:
                    cell ^= matrix[i - 1][j - 1]
                matrix[i][j] = cell
                if len(minHeap) < k:
                    heapq.heappush(minHeap, cell)
                else:
                    heapq.heappushpop(minHeap, cell)
        return minHeap[0]
