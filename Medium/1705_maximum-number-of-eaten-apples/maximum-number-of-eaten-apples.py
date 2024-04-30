class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        ans = i = 0
        batches = []
        while i < len(apples) or batches:
            if i < len(apples) and apples[i]:  # Harvest the apples
                heapq.heappush(batches, [i + days[i], apples[i]])
            while batches and (batches[0][0] <= i or not batches[0][1]):  # The first batch of apples are either rotten or eaten
                heapq.heappop(batches)
            if batches:  # Eat an apple from the first batch
                batches[0][1] -= 1
                ans += 1
            i += 1
        return ans
