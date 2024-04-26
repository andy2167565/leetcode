class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # Reference: https://leetcode.com/problems/find-latest-group-of-size-m/solutions/806786/java-c-python-count-the-length-of-groups-o-n/
        if m == len(arr):
            return m
        ans, length = -1, [0] * (len(arr) + 2)  # length[i]: The length of the group including i-th bit
        for i, num in enumerate(arr):
            left, right = length[num - 1], length[num + 1]
            if m in (left, right):  # One of the group has length m
                ans = i
            length[num - left] = length[num + right] = left + right + 1  # Only update the length values on the leftmost and the rightmost bits of the group
        return ans
