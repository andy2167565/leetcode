class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
# Tree Characteristics:
# 1. Number of edges = Number of nodes - 1 and acyclic (i.e directed graph with no cycle)
# 2. Number of edges = Number of nodes - 1 and connected (Note: the 1st characteristic implies that the connected graph has no cycle)
#======== <Solution 1> ========#
        if n - 1 != len(edges): return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        return dfs(0) or len(visited) == n  # If the graph is connected then all vertices must be visited

#======== <Solution 2> ========#
        if n - 1 != len(edges): return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited, stack = set(), [0]
        while stack:
            node = stack.pop()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return len(visited) == n

#======== <Solution 3> ========#
        import collections
        if n - 1 != len(edges): return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited, queue = set(), collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return len(visited) == n

#======== <Solution 4> ========#
        if n - 1 != len(edges): return False
        parent = list(range(n))
        def find(x):
            return x if parent[x] == x else find(parent[x])
        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y
        return all(map(union, edges))
