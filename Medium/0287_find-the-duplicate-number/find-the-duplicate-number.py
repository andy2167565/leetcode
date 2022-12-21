class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
# Reference: https://leetcode.com/problems/find-the-duplicate-number/solutions/1892921/9-approaches-count-hash-in-place-marked-sort-binary-search-bit-mask-fast-slow-pointers/
#======== <Solution 1> ========#
        count = [0] * len(nums)
        for num in nums:
            if count[num]:
                return num
            count[num] += 1

#======== <Solution 2> ========#
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

#======== <Solution 3> ========#
        for num in nums:
            i = abs(num)  # Use absolute value of num as index
            if nums[i] < 0:  # num at index i has been marked previously
                return i
            nums[i] *= -1  # Marked as visited

#======== <Solution 4> ========#
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

#======== <Solution 5> ========#
        for i, num in enumerate(sorted(nums)):
            if i == num:
                return num

#======== <Solution 6> ========#
        l, r = 1, len(nums) - 1
        while l < r:
            mid, count = l + (r - l) // 2, 0
            for num in nums:  # Count numbers that are smaller than or equal to mid
                if num <= mid:
                    count += 1
            if count > mid:  # According to the Pigeonhole Principle, if count is greater than mid, repeated elements are in the interval [l, mid]
                r = mid
            else:  # Otherwise, the repeated elements are in the interval [mid + 1, r]
                l = mid + 1
        return l

#======== <Solution 7> ========#
        seen = 0
        for num in nums:
            if seen & (1 << num):
                return num
            seen |= 1 << num  # Mark num as a binary digit in seen
            # e.g. nums = [1, 3, 4, 2, 2]
            #      num   seen   (1 << num)   seen & (1 << num)   seen | (1 << num)
            #       1       0           10                   0                  10
            #       3      10         1000                   0                1010
            #       4    1010        10000                   0               11010
            #       2   11010          100                   0               11110
            #       2   11110          100                   1

#======== <Solution 8> ========#
        # Reference 1: https://leetcode.com/problems/find-the-duplicate-number/solutions/127594/official-solution/
        # Reference 2: https://leetcode.com/problems/linked-list-cycle-ii/solutions/1701055/java-c-python-best-explanation-ever-happen-s-for-this-problem/
        # Reduce the problem to the following: Given a linked list, return the node where the cycle begins
        # Linked list: num -> nums[num] -> nums[nums[num]] -> ...
        # There is a duplicate number => There is a cycle in the list
        # The entrance to the cycle => The duplicate number we want
        slow = fast = nums[0]
        while True:  # Find the intersection point of the two pointers
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]
        while slow != fast:  # Find the entrance to the cycle
            slow, fast = nums[slow], nums[fast]
        return slow
