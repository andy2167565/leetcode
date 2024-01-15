class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        import collections, heapq
        graph = collections.defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        pq = [(-1.0, start_node)]
        heapq.heapify(pq)
        while pq:
            currProb, currNode = heapq.heappop(pq)
            currProb *= -1
            if currNode == end_node:
                return currProb
            for nextNode, nextProb in graph[currNode]:
                nextProb *= currProb
                if nextProb > maxProb[nextNode]:
                    maxProb[nextNode] = nextProb
                    heapq.heappush(pq, (-nextProb, nextNode))
        return 0.0
