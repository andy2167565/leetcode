class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        import collections
        children = collections.defaultdict(list)
        ans = [[] for _ in range(n)]
        for x, y in edges:
            children[x].append(y)

        def dfs(parent, node):
            for child in children[node]:
                if ans[child] and ans[child][-1] == parent:
                    continue
                ans[child].append(parent)
                dfs(parent, child)

        for i in range(n):
            dfs(i, i)
        return ans
