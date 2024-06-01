class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Reference: https://leetcode.com/problems/get-the-maximum-score/solutions/767987/java-c-python-two-pointers-o-1-space/
        i = j = sum1 = sum2 = 0
        m, n = len(nums1), len(nums2)
        while i < m or j < n:
            if i < m and (j == n or nums1[i] < nums2[j]):  # nums1 has a smaller element
                sum1 += nums1[i]
                i += 1
            elif j < n and (i == m or nums1[i] > nums2[j]):  # nums2 has a smaller element
                sum2 += nums2[j]
                j += 1
            else:  # The elements in both arrays are the same
                sum1 = sum2 = max(sum1, sum2) + nums1[i]  # Choose the path with larger sum
                i += 1
                j += 1
        return max(sum1, sum2) % (10**9 + 7)
