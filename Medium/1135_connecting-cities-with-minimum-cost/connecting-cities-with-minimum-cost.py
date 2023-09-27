class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import collections, heapq
        graph = collections.defaultdict(list)
        for x, y, cost in connections:
            graph[x].append((cost, y))
            graph[y].append((cost, x))
        ans, visited, queue = 0, set(), [(0, n)]  # Arrive at city n with cost 0
        while queue and len(visited) < n:  # Exit if all cities are visited
            cost, city = heapq.heappop(queue)  # cost is always the minimum in queue
            if city not in visited:
                visited.add(city)
                ans += cost
                for edge_cost, next_city in graph[city]:
                    heapq.heappush(queue, (edge_cost, next_city))
        return ans if len(visited) == n else -1

#======== <Solution 2> ========#
        def find(city):  # Recursively reset city's parent to its parent's parent
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        def union(city1, city2):
            root1, root2 = find(city1), find(city2)
            if root1 == root2:
                return False
            parent[root2] = root1  # Always join roots
            return True
        
        parent = {city: city for city in range(1, n + 1)}  # Initially each city is its own set
        connections.sort(key=lambda x: x[2])  # Sort connections so we are always picking minimum cost edge
        ans = 0
        for x, y, cost in connections:
            if union(x, y):
                ans += cost
        root = find(n)  # Check if all cities are connected
        return ans if all(root == find(city) for city in range(1, n + 1)) else -1
