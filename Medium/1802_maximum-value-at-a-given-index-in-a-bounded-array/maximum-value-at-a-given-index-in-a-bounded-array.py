class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/solutions/1119801/java-c-python-binary-search/
        def check(num):  # Check the minimum sum when nums[index] == num
            l_offset = max(num - index, 0)
            res = (num + l_offset) * (num - l_offset + 1) // 2
            r_offset = max(num - ((n - 1) - index), 0)
            res += (num + r_offset) * (num - r_offset + 1) // 2
            return res - num

        maxSum -= n  # All nums[i] only need to be greater than or equal to 0
        l, r = 0, maxSum
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid) <= maxSum:
                l = mid
            else:
                r = mid - 1
        return l + 1
