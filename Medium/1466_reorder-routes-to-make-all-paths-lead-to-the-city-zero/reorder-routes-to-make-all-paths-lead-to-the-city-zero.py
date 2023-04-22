class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import collections
        graph, roads = collections.defaultdict(list), set()
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))
        def dfs(source, target, ans=0):
            ans += (source, target) in roads  # Route source -> target needs to be changed
            for neighbor in graph[target]:
                if neighbor != source:
                    ans += dfs(target, neighbor)
            return ans
        return dfs(-1, 0)

#======== <Solution 2> ========#
        import collections
        graph = collections.defaultdict(dict)
        for a, b in connections:
            graph[a][b] = 1  # Route a -> b needs to be changed
            graph[b][a] = 0
        visited = set()
        def dfs(city):
            visited.add(city)
            return sum(graph[city][neighbor] + dfs(neighbor) for neighbor in graph[city] if neighbor not in visited)
        return dfs(0)

#======== <Solution 3> ========#
        import collections
        graph = collections.defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # Route a -> b needs to be changed
            graph[b].append((a, 0))
        q, visited, ans = collections.deque([0]), {0}, 0
        while q:
            for neighbor, cost in graph[q.popleft()]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    ans += cost
                    q.append(neighbor)
        return ans
