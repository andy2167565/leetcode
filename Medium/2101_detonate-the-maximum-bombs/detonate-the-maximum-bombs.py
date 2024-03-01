class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        import collections
        ans, graph = 0, collections.defaultdict(list)
        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, rj) in enumerate(bombs):
                if i != j and (xi - xj)**2 + (yi - yj)**2 <= ri**2:  # Bomb j is in the range of bomb i
                    graph[i].append(j)
        
        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)
        
        for i in range(len(bombs)):  # Detonate each bomb and determine which one has the greatest impact on the surrounding bombs
            detonated = {i}
            dfs(i, detonated)
            ans = max(ans, len(detonated))
        return ans
