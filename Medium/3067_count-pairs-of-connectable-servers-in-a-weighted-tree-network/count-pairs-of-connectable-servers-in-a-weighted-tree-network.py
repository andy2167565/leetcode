class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        import collections, itertools
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        def dfs(node, parent, weight):
            if not weight % signalSpeed:
                self.length += 1
            for adj, w in graph[node]:
                if adj != parent:
                    dfs(adj, node, weight + w)
        
        ans = []
        for node in range(len(edges) + 1):
            lengths = []  # The lengths of the routes starting from node
            for adj, weight in graph[node]:
                self.length = 0
                dfs(adj, node, weight)
                lengths.append(self.length)
            ans.append(sum(i * j for i, j in itertools.combinations(lengths, 2)))
        return ans
