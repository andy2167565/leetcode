class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
# Reference: https://leetcode.com/problems/advantage-shuffle/solutions/149842/python-greedy-solution-using-sort/
#======== <Solution 1> ========#
        import collections
        nums1 = collections.deque(sorted(nums1))  # Sort nums1 increasingly as candidates
        for num2, i in sorted([(num2, i) for i, num2 in enumerate(nums2)], reverse=True):  # Sort nums2 decreasingly
            nums2[i] = nums1.pop() if num2 < nums1[-1] else nums1.popleft()  # Choose largest num1 that is larger than largest num2, otherwise choose smallest num1 instead
        return nums2

#======== <Solution 2> ========#
        import bisect
        nums1.sort()
        ans = []
        for num2 in nums2:
            idx = bisect.bisect_right(nums1, num2)
            ans.append(nums1.pop(0) if idx == len(nums1) else nums1.pop(idx))
        return ans
