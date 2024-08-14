class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-pairs-satisfying-inequality/solutions/2646606/python-reverse-pairs/
        import sortedcontainers
        ans, arr = 0, sortedcontainers.SortedList()
        for num1, num2 in zip(nums1, nums2):
            ans += arr.bisect_right(num1 - num2 + diff)
            arr.add(num1 - num2)
        return ans
