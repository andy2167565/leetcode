class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Reference: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/solutions/490312/java-c-python-easy-floyd-algorithm/
        dist = [[float('inf')] * n for _ in range(n)]  # dist[i][j]: The distance between cities i and j
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w
        for i in range(n):  # The distance from each city to itself is 0
            dist[i][i] = 0
        for k in range(n):  # Iterate all middle points k for each pair (i, j)
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        res = {sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
        return res[min(res)]
