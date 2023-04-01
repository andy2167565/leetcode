class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Reference: https://leetcode.com/problems/count-the-hidden-sequences/solutions/1709755/java-c-python-straight-forward-solution-with-explantion/
        import itertools
        hidden = list(itertools.accumulate(differences, initial=0))
        return max((upper - lower) - (max(hidden) - min(hidden)) + 1, 0)
