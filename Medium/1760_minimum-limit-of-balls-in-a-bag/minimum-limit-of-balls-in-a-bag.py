class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/solutions/1064548/java-c-python-binary-search/
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if sum((num - 1) // mid for num in nums) > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l
