class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/shortest-cycle-in-a-graph/solutions/3366362/java-python-3-bfs-within-dfs/
        import collections
        ans, graph = float('inf'), collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        for root in range(n):
            dq, parent, dist = collections.deque([root]), [-1] * n, [float('inf')] * n  # dist[i]: The distance from root to i
            dist[root] = 0
            while dq:
                node = dq.popleft()
                for adj in graph[node]:
                    if dist[adj] == float('inf'):
                        dist[adj], parent[adj] = dist[node] + 1, node
                        dq.append(adj)
                    elif parent[adj] != node and parent[node] != adj:
                        ans = min(ans, dist[node] + dist[adj] + 1)
        return -1 if ans == float('inf') else ans
