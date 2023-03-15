class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, count=1):
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    count += dfs(adj)
            return count

        import collections
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        unreachable_pairs = total_nodes = 0
        for i in range(n):
            if i not in visited:
                reachable_nodes = dfs(i)
                unreachable_pairs += reachable_nodes * total_nodes
                total_nodes += reachable_nodes
        return unreachable_pairs
