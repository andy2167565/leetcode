class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/decode-xored-permutation/solutions/1031107/java-c-python-straight-forward-solution/
        import functools, operator, itertools
        first = functools.reduce(operator.ixor, encoded[::-2] + list(range(len(encoded) + 2)))
        return list(itertools.accumulate([first] + encoded, operator.ixor))
