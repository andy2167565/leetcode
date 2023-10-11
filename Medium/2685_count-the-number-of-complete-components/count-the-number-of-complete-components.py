class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        import collections
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        ans, visited = 0, set()
        for i in range(n):
            if i not in visited:
                bfs = [i]
                visited.add(i)
                for j in bfs:
                    for adj in graph[j]:
                        if adj not in visited:
                            bfs.append(adj)
                            visited.add(adj)
                ans += all(len(graph[j]) == len(bfs) - 1 for j in bfs)
        return ans
