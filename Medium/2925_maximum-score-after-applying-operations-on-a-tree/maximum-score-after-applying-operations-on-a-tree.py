class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        import collections

        def dfs(node, parent):
            if node and graph[node] == [parent]:  # Leaf node
                return values[node]
            child_sum = sum(dfs(child, node) for child in graph[node] if child != parent)  # The sum of value of child nodes
            return min(child_sum, values[node])

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return sum(values) - dfs(0, -1)
