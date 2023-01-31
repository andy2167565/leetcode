class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/3099885/day-26-simple-bfs-easiest-beginner-friendly-solution/
        import collections
        adj = [[] for _ in range(n)]  # adj[i]: Pairs of adjacent node and the price to arrive it for each node i
        for a, b, p in flights:
            adj[a].append((b, p))
        q = collections.deque([(src, 0)])  # Current node and the cost needed to reach it from src
        minCost = [float('inf') for _ in range(n)]  # minCost[i]: The minimum cost to reach node i
        stops = 0
        while q and stops <= k:
            for _ in range(len(q)):
                node, cost = q.popleft()
                for neighbor, price in adj[node]:
                    if cost + price < minCost[neighbor]:  # Path with less cost
                        minCost[neighbor] = cost + price
                        q.append((neighbor, minCost[neighbor]))
            stops += 1
        return minCost[dst] if minCost[dst] != float('inf') else -1

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/3099854/dynamic-programming-solution-with-video/
        dp = [[sys.maxsize for _ in range(n)] for _ in range(k + 2)]  # Table where columns are cities, rows are steps (not stops), and values are costs to travel from src to this city
        for i in range(k + 2):  # The costs required to travel from src to src is 0 with any steps
            dp[i][src] = 0
        for i in range(1, k + 2):
            for a, b, p in flights:
                if dp[i - 1][a] != sys.maxsize:  # Node a is already visited in step (i - 1)
                    dp[i][b] = min(dp[i][b], dp[i - 1][a] + p)  # Update the cost to node b with 1 step forward
        return dp[k + 1][dst] if dp[k + 1][dst] != sys.maxsize else -1
