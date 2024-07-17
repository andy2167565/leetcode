class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        import collections
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        ans, degree = float('inf'), {node: len(graph[node]) for node in graph}
        for u, v in edges:
            for w in graph[u] & graph[v]:
                ans = min(ans, degree[u] + degree[v] + degree[w] - 6)
        return ans if ans < float('inf') else -1
