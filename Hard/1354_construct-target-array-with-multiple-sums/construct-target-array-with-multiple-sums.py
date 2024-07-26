class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Reference: https://leetcode.com/problems/construct-target-array-with-multiple-sums/solutions/510256/java-c-python-backtrack-oj-is-wrong/
        import heapq
        total = sum(target)
        heap = [-num for num in target]
        heapq.heapify(heap)
        while True:
            num = -heapq.heappop(heap)
            total -= num
            if 1 in (num, total):
                return True
            if num < total or not total or not num % total:
                return False
            num %= total
            total += num
            heapq.heappush(heap, -num)
