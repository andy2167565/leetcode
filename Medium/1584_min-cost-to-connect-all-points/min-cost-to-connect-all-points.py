class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        ans, visited, minheap, min_dist = 0, set(), [(0, 0)], {0: 0}
        while minheap:
            cost, point = heapq.heappop(minheap)  # Get the point with the minimum cost
            if point not in visited:
                visited.add(point)
                ans += cost
                for next_point in range(len(points)):
                    if next_point not in visited:
                        dist = abs(points[point][0] - points[next_point][0]) + abs(points[point][1] - points[next_point][1])
                        if dist < min_dist.get(next_point, float('inf')):
                            min_dist[next_point] = dist  # Update the minimum distance of next point
                            heapq.heappush(minheap, (dist, next_point))
        return ans
