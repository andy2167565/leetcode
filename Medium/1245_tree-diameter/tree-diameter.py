class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        import collections
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        length = 0
        while len(graph) > 2:
            toRemove = []
            for node in graph:  # Collect all end points
                if len(graph[node]) == 1:
                    toRemove.append(node)
            for node in toRemove:  # Remove one level starting from end points
                adj = graph[node].pop()
                graph.pop(node)
                graph[adj].remove(node)
            length += 2
        return length + 1 if len(graph) == 2 else length
