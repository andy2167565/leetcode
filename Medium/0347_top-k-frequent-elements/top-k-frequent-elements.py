class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#======== <Solution 1> ========#
        import collections
        return [num for num, count in collections.Counter(nums).most_common(k)]

# Reference: https://leetcode.com/problems/top-k-frequent-elements/discuss/484980/Python-Explained-Two-Simple-Heap-solutions
#======== <Solution 2> ========#
        import collections, heapq
        maxHeap = [(-count, num) for num, count in collections.Counter(nums).items()]
        heapq.heapify(maxHeap)
        return [heapq.heappop(maxHeap)[1] for _ in range(k)]

#======== <Solution 3> ========#
        import collections, heapq
        counter = collections.Counter(nums)
        heap = [(count, num) for num, count in list(counter.items())[:k]]
        heapq.heapify(heap)
        for num, count in list(counter.items())[k:]:
            heapq.heappushpop(heap, (count, num))
        return [num for _, num in heap]

# Reference (Explanation): https://leetcode.com/problems/top-k-frequent-elements/discuss/1927648/One-OF-THE-best-EXPLANATION
#======== <Solution 4> ========#
        import collections
        n, ans = len(nums), []
        bucket = [[] for _ in range(n + 1)]
        for num, count in collections.Counter(nums).items():
            bucket[count].append(num)
        while k:
            while not bucket[n]:
                n -= 1
            ans.extend(bucket[n])
            k -= len(bucket[n])
            n -= 1
        return ans
