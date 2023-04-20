class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/number-of-operations-to-make-network-connected/solutions/477679/python-count-the-connected-networks/
        if len(connections) < n - 1:  # Not enough cables
            return -1
        graph = [set() for _ in range(n)]
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        seen = [0] * n
        def dfs(node):
            if seen[node]:
                return 0
            seen[node] = 1
            for adj in graph[node]:
                dfs(adj)
            return 1
        return sum(dfs(i) for i in range(n)) - 1  # The number of operations = The number of connected networks - 1

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/number-of-operations-to-make-network-connected/solutions/477835/6-lines-clean-unicode-find/
        if len(connections) < n - 1:
            return -1
        s = ''.join(map(chr, range(n)))  # Convert each integer to its unicode character
        for a, b in connections:  # Computers in the same network will be assigned the same character
            s = s.replace(s[a], s[b])
        return len(set(s)) - 1
