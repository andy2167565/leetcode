class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-number-of-k-divisible-components/solutions/4109948/python-cut-leaf-or-merge-with-parent-explained/
        import collections
        if n <= 1:
            return 1
        ans, graph = 0, collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        q = collections.deque(node for node, arr in graph.items() if len(arr) == 1)  # Start with leaves
        while q:  # Cut leaves layer by layer
            for _ in range(len(q)):
                node = q.popleft()
                parent = next(iter(graph[node])) if graph[node] else -1
                if parent >= 0:
                    graph[parent].remove(node)
                if not values[node] % k:  # Separate a correct component
                    ans += 1
                else:  # Add to parent
                    values[parent] += values[node]
                if parent >= 0 and len(graph[parent]) == 1:  # Update queue with new leaves
                    q.append(parent)
        return ans
