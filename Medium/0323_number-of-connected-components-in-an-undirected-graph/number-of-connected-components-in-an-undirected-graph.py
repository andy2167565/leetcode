class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
# Reference: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/solutions/319459/python3-unionfind-dfs-bfs-solution/
#======== <Solution 1> ========#
        def dfs(node):
            if not visited[node]:
                visited[node] = 1  # Marked as visited
                for adj in graph[node]:  # Check all connected nodes
                    dfs(adj)

        ans, visited, graph = 0, [0] * n, [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        for i in range(n):
            if not visited[i]:
                dfs(i)  # Mark every connected node as visited
                ans += 1
        return ans

#======== <Solution 2> ========#
        import collections
        def bfs(node):
            queue = collections.deque([node])
            while queue:
                node = queue.popleft()
                for adj in graph[node]:
                    if adj not in seen:
                        seen.add(adj)
                        queue.append(adj)

        ans, seen, graph = 0, set(), collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        for i in range(n):
            if i not in seen:
                seen.add(i)
                bfs(i)
                ans += 1
        return ans

#======== <Solution 3> ========#
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(edge):
            a, b = list(map(find, edge))
            if a != b:  # The nodes in edge do not have the same parent
                if rank[a] > rank[b]:
                    parent[b] = a
                else:
                    parent[a] = b
                    if rank[a] == rank[b]:
                        rank[b] += 1

        parent, rank = list(range(n)), [0] * n
        list(map(union, edges))
        return len(set(map(find, parent)))

#======== <Solution 4> ========#
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(edge):
            a, b = list(map(find, edge))
            if a != b:
                parent[a] = b

        parent = list(range(n))
        list(map(union, edges))
        return len(set(map(find, parent)))
