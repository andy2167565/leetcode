class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        import collections
        def dfs(curr, prev, t):
            ways = [nxt for nxt in graph[curr] if nxt != prev]
            if curr == target:  # Reached the target
                if not ways:  # target is the end of route
                    return 1
                return not t  # Check if the time has been run out
            if not t:  # The time has been run out before reaching the target
                return 0
            return max([dfs(nxt, curr, t - 1) * (1 / len(ways)) for nxt in ways], default=0)
        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return dfs(1, 1, t)
