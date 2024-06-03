class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/find-eventual-safe-states/solutions/128872/python-easy-peasy-11-lines-very-simple-and-clear-solution-192-ms-beats-100/
        seen, safe = set(), set()

        def dfs(node):
            if node in seen:
                return node in safe
            seen.add(node)
            if all(dfs(nxt) for nxt in graph[node]):
                safe.add(node)
                return True

        return filter(dfs, range(len(graph)))
