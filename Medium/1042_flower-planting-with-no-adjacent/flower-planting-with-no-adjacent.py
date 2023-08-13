class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans, graph = [0] * n, [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        for node in range(n):
            ans[node] = ({1, 2, 3, 4} - {ans[adj] for adj in graph[node]}).pop()  # Choose a type not planted by adjacent gardens
        return ans
