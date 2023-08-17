class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, curr_dist, dist):  # Collect the distances from node to each node i
            while node != -1 and dist[node] == -1:
                dist[node] = curr_dist
                curr_dist += 1
                node = edges[node]
        ans, min_dist, n = -1, float('inf'), len(edges)
        dist1, dist2 = [-1] * n, [-1] * n
        dfs(node1, 0, dist1)
        dfs(node2, 0, dist2)
        for curr in range(n):  # Iterate all destinations
            if min(dist1[curr], dist2[curr]) >= 0 and max(dist1[curr], dist2[curr]) < min_dist:
                min_dist = max(dist1[curr], dist2[curr])
                ans = curr
        return ans
