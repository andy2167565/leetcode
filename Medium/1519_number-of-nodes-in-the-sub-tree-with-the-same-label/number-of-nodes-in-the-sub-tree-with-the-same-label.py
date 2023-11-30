class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        import collections
        def dfs(node, parent):
            counter = collections.Counter(labels[node])
            for child in graph[node]:
                if child != parent:
                    counter += dfs(child, node)
            ans[node] = counter[labels[node]]
            return counter
        
        graph, ans = collections.defaultdict(list), [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dfs(0, -1)
        return ans
