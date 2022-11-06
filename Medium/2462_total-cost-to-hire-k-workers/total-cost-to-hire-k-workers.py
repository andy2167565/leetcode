class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq
        l, r, ans = candidates, len(costs) - 1 - candidates, 0
        leftHeap, rightHeap = costs[:candidates], costs[max(candidates, len(costs) - candidates):]  # rightHeap is the rest of costs after leftHeap if len(costs) <= candidates * 2
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)
        for _ in range(k):
            # (not rightHeap) or (leftHeap and rightHeap): Choose worker from leftHeap
            # not leftHeap: Choose worker from rightHeap
            # l <= r: There are still workers who have not been included as candidates
            if not rightHeap or leftHeap and leftHeap[0] <= rightHeap[0]:
                ans += heapq.heappop(leftHeap)
                if l <= r:
                    heapq.heappush(leftHeap, costs[l])
                    l += 1
            else:
                ans += heapq.heappop(rightHeap)
                if l <= r:
                    heapq.heappush(rightHeap, costs[r])
                    r -= 1
        return ans
