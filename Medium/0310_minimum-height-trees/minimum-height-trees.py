class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
        if n == 1: return [0]
        graph = [set() for _ in range(n)]  # graph[i] indicates adjacent vertices of vertex i
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = [i for i in range(n) if len(graph[i]) == 1]  # Vertices with only 1 edge attached to it
        while n > 2:  # Number of middle vertices is 1 or 2 depending on the parity of n
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:  # Break the edge between leaf and its adjacent vertex
                adj = graph[leaf].pop()
                graph[adj].remove(leaf)
                if len(graph[adj]) == 1:  # adj becomes new leaf
                    newLeaves.append(adj)
            leaves = newLeaves
        return leaves
