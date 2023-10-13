class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # Reference: https://leetcode.com/problems/circular-permutation-in-binary-representation/solutions/414203/java-c-python-4-line-gray-code/
        return [start ^ i ^ i >> 1 for i in range(1 << n)]
