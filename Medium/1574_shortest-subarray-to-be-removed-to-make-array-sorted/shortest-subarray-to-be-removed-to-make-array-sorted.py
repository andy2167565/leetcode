class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Reference: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/830699/python-two-pointers-approach-with-explanation/
        j = len(arr) - 1
        while j and arr[j - 1] <= arr[j]:  # Search for non-decreasing suffix
            j -= 1
        i, ans = 0, j
        while i < j and (not i or arr[i - 1] <= arr[i]):  # Search for non-decreasing prefix
            while j < len(arr) and arr[i] > arr[j]:  # Adjust the start of suffix according to prefix
                j += 1
            ans = min(ans, j - i - 1)  # Merge prefix and suffix
            i += 1
        return ans
