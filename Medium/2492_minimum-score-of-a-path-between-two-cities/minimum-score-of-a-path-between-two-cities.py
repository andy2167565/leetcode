class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/discuss/2875034/Python-connected-component-of-1-(explained)
        import collections
        graph = collections.defaultdict(dict)
        for a, b, distance in roads:  # Create a graph of cities. Each graph[i] is a dictionary that contains adjacent cities of i with corresponding distance.
            graph[a][b] = graph[b][a] = distance
        ans, visited, dq = float('inf'), {1}, collections.deque([1])  # Start from city 1
        while dq:
            city = dq.popleft()
            for adjacent, distance in graph[city].items():
                if adjacent not in visited:
                    dq.append(adjacent)
                    visited.add(adjacent)
                ans = min(ans, distance)
        return ans
