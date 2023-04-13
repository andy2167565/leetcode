class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # Color each node with 0 or 1
        def dfs(node):
            for adj in graph[node]:
                if adj in color:
                    if color[adj] == color[node]:  # Adjacent node already has the same color as current node
                        return False
                else:
                    color[adj] = 1 - color[node]  # Assign adjacent node with color different from current node
                    if not dfs(adj):
                        return False
            return True
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False
        return True
