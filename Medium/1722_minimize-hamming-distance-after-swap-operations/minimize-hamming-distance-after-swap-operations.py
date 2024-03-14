class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/solutions/1009867/python-dfs-solution/
        import collections
        ans = n = len(source)
        graph, seen = collections.defaultdict(set), set()
        for a, b in allowedSwaps:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(i):
            seen.add(i)
            connected.append(i)
            for j in graph[i]:
                if j not in seen:
                    dfs(j)

        for i in range(n):
            if i not in seen:
                connected = []
                dfs(i)
                counter_source = collections.Counter(source[j] for j in connected)
                counter_target = collections.Counter(target[j] for j in connected)
                ans -= sum((counter_source & counter_target).values())
        return ans
