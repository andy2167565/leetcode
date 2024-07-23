class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/solutions/2831676/c-java-python3-simple-dfs-o-n/
        import collections, math
        graph = collections.defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        self.ans = 0

        def dfs(city, prev, people=1):
            for adj in graph[city]:
                if adj != prev:
                    people += dfs(adj, city)
            self.ans += (math.ceil(people / seats) if city else 0)
            return people

        dfs(0, 0)
        return self.ans
