class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # Reference: https://leetcode.com/problems/longest-cycle-in-a-graph/solutions/3341780/clean-codes-full-explanation-d-f-s-c-java-python3/
        ans, time, time_visited = -1, 1, [0] * len(edges)  # The time at which each node was first visited
        for curr in range(len(edges)):
            if not time_visited[curr]:
                start, nxt = time, curr
                while nxt != -1 and not time_visited[nxt]:  # Stop when the end of the path is reached or a visited node is encountered
                    time_visited[nxt], nxt = time, edges[nxt]
                    time += 1
                if nxt != -1 and time_visited[nxt] >= start:  # A cycle is found
                    ans = max(ans, time - time_visited[nxt])
        return ans
