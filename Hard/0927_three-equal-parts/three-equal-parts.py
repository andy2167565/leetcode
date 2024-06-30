class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/three-equal-parts/solutions/1343665/python-o-n-fast-solution-explained/
        one_count = arr.count(1)
        if not one_count:  # Any split would satisfy
            return [0, 2]
        if not one_count % 3:  # Number of ones in three equal parts must be the same
            one_index = [i for i, num in enumerate(arr) if num]
            s1, s2, s3 = one_index[0], one_index[one_count // 3], one_index[2 * one_count // 3]  # The index of first one in each part
            e1, e2, e3 = one_index[one_count // 3 - 1], one_index[2 * one_count // 3 - 1], one_index[-1]  # The index of last one in each part
            trailing_zeros = len(arr) - 1 - e3
            if e1 + trailing_zeros < s2 and e2 + trailing_zeros < s3 and arr[s1:e1] == arr[s2:e2] == arr[s3:e3]:
                return [e1 + trailing_zeros, e2 + trailing_zeros + 1]
        return [-1, -1]
