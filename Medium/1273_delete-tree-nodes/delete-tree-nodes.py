class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        import collections
        graph = collections.defaultdict(set)
        for i, p in enumerate(parent[1:], 1):
            graph[p].add(i)
        def dfs(node):
            total, count = value[node], 1
            for child in graph[node]:
                t, c = dfs(child)
                total += t
                count += c
            return total, count if total else 0
        return dfs(0)[1]
