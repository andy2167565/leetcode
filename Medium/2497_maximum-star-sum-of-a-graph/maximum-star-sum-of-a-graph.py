class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
# Reference: https://leetcode.com/problems/maximum-star-sum-of-a-graph/solutions/2897917/python-it-s-bidirectional-explained/
#======== <Solution 1> ========#
        import collections
        graph = collections.defaultdict(set)
        for a, b in edges:
            if vals[a] > 0: graph[b].add(a)
            if vals[b] > 0: graph[a].add(b)
        stars = []
        for i, v in enumerate(vals):
            adjs = [vals[j] for j in graph[i]]  # Positive values of adjacent nodes of i
            adjs.sort(reverse=True)
            stars.append(v + sum(adjs[:k]))
        return max(stars)

#======== <Solution 2> ========#
        import collections
        graph = collections.defaultdict(set)
        for a, b in edges:
            if vals[a] > 0: graph[b].add(a)
            if vals[b] > 0: graph[a].add(b)
        return max(v + sum(sorted(vals[j] for j in graph[i])[-k:]) for i, v in enumerate(vals))
