class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        import collections
        def dfs(node, prev):  # Propagate the nodes which have apples
            for neighbor in graph[node]:
                if neighbor != prev and dfs(neighbor, node):
                    hasApple[node] = True
            return hasApple[node]
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dfs(0, -1)
        return (sum(hasApple) - hasApple[0]) * 2
