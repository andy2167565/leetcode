class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/shortest-path-with-alternating-colors/solutions/339964/java-python-bfs/
        graph = [[[], []] for _ in range(n)]
        for a, b in redEdges:
            graph[a][0].append(b)
        for u, v in blueEdges:
            graph[u][1].append(v)
        path = [[0, 0]] + [[n * 2, n * 2] for _ in range(n - 1)]
        bfs = [[0, 0], [0, 1]]
        for idx, color in bfs:
            for adj in graph[idx][color]:
                if path[adj][color] == n * 2:
                    path[adj][color] = path[idx][1 - color] + 1
                    bfs.append([adj, 1 - color])
        return [l if l < n * 2 else -1 for l in map(min, path)]
