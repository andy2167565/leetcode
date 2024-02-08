class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        import collections
        n, graph = len(patience), collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited, min_cost, queue = {0}, [-1] * n, collections.deque([(0, 0)])
        while queue:
            node, edge = queue.popleft()
            min_cost[node] = 2 * edge  # The cost is twice edge
            for adj in graph[node]:
                if adj not in visited:
                    visited.add(adj)
                    queue.append((adj, edge + 1))
        ans = 0
        for cost, wait in zip(min_cost[1:], patience[1:]):
            last_send = cost - (cost % wait if cost % wait else wait)  # The last time a request was sent before receiving a response
            ans = max(ans, last_send + cost)
        return ans + 1
