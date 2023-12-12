class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        ans, maxHeap = '', []
        for count, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count:
                heapq.heappush(maxHeap, (count, ch))
        while maxHeap:
            count, ch = heapq.heappop(maxHeap)  # Always start with the char that has the most number of it
            if len(ans) > 1 and ans[-1] == ans[-2] == ch:  # Already appended two same chars continuously
                if not maxHeap:  # No other chars can be added
                    break
                count2, ch2 = heapq.heappop(maxHeap)  # Add the second most char
                ans += ch2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, ch2))
            else:
                ans += ch
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, ch))
        return ans
