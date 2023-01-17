class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
#======== <Solution 1> ========#
        return sorted(nums)[-k]

#======== <Solution 2> ========#
        import heapq
        minHeap = nums[:k]
        heapq.heapify(minHeap)
        for num in nums[k:]:
            heapq.heappushpop(minHeap, num)
        return minHeap[0]

#======== <Solution 3> ========#
        import heapq
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]

#======== <Solution 4> ========#
        import heapq
        return heapq.nlargest(k, nums)[-1]

#======== <Solution 5> ========#
        import random
        pivot, small, equal, large = random.choice(nums), [], [], []
        for num in nums:  # Split nums by each element compared with pivot
            if num < pivot:
                small.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                large.append(num)
        if k <= len(large):  # kth largest element is larger than pivot
            return self.findKthLargest(large, k)
        if k > len(large) + len(equal):  # kth largest element is smaller than pivot
            return self.findKthLargest(small, k - len(large) - len(equal))
        return pivot  # kth largest element is equal to pivot
