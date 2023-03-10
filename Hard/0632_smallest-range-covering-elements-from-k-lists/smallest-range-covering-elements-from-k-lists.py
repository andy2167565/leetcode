class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/solutions/104904/python-heap-based-solution/
        import heapq
        pq, right = [], float('-inf')  # pq collects minimum number of each list in nums in each round
        for i, ls in enumerate(nums):
            pq.append((ls[0], i, 0))  # (minimum number of ls, index of ls in nums, index of number in ls)
            right = max(right, ls[0])
        heapq.heapify(pq)  # Min heap
        ans = float('-inf'), float('inf')
        while pq:
            left, i, j = heapq.heappop(pq)  # left is current minimum number among k lists
            if right - left < ans[1] - ans[0]:  # Update with smaller range
                ans = left, right
            if j + 1 == len(nums[i]):  # nums[i] is exhausted
                return ans
            next_num = nums[i][j + 1]  # Next number in nums[i]
            right = max(right, next_num)  # Update current maximum number among k lists
            heapq.heappush(pq, (next_num, i, j + 1))

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/solutions/104905/python-straightforward-with-explanation/
        ans = float('-inf'), float('inf')
        left = float('inf')
        for right in sorted(set(num for ls in nums for num in ls))[::-1]:  # Flatten nums in descending order
            for ls in nums:
                while ls and right < ls[-1]:  # Remove numbers that are larger than current maximum number
                    ls.pop()
                if not ls:  # ls is exhausted
                    return ans
                left = min(left, ls[-1])  # Update current minimum number among k lists
            if right - left <= ans[1] - ans[0]:  # Include equal range since we start from maximum number of each list in nums
                ans = left, right
        return ans
