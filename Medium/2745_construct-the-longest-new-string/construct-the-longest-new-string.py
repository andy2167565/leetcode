class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # Reference 1: https://leetcode.com/problems/construct-the-longest-new-string/solutions/3677601/c-java-python-o-1-complexity-with-explanation/
        # Reference 2: https://leetcode.com/problems/construct-the-longest-new-string/solutions/3677618/java-c-python-1-line-o-1/
        return (min(x, y) * 2 + (x != y) + z) * 2
