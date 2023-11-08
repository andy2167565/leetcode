class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(nums1, nums2):
            max_diff = curr_diff = 0
            for num1, num2 in zip(nums1, nums2):
                curr_diff = max(0, curr_diff + num1 - num2)
                max_diff = max(max_diff, curr_diff)
            return sum(nums2) + max_diff
        return max(kadane(nums1, nums2), kadane(nums2, nums1))
