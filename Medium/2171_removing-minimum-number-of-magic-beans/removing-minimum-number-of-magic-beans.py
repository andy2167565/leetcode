class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # Reference: https://leetcode.com/problems/removing-minimum-number-of-magic-beans/solutions/1766764/c-java-python3-sorting-4-lines/
        return sum(beans) - max((len(beans) - i) * num for i, num in enumerate(sorted(beans)))
