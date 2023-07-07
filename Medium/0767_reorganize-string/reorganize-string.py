class Solution:
    def reorganizeString(self, s: str) -> str:
        import collections, heapq
        ans, prev_ch, prev_count, maxHeap = '', '', 0, [(-count, ch) for ch, count in collections.Counter(s).items()]
        heapq.heapify(maxHeap)
        while maxHeap:
            count, ch = heapq.heappop(maxHeap)
            ans += ch
            if prev_count < 0:  # There are some prev_ch left as candidates
                heapq.heappush(maxHeap, (prev_count, prev_ch))
            count += 1
            prev_count, prev_ch = count, ch
        return ans if len(ans) == len(s) else ''  # Make sure all the characters in s are used
