class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Reference: https://leetcode.com/problems/furthest-building-you-can-reach/solutions/918515/java-c-python-priority-queue/
        import heapq
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:  # Require a ladder or some bricks
                heapq.heappush(heap, diff)
            if len(heap) > ladders:  # Use bricks for the move with minimum difference
                bricks -= heapq.heappop(heap)
            if bricks < 0:  # Run out of ladders and bricks
                return i
        return len(heights) - 1
