class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Reference: https://leetcode.com/problems/mirror-reflection/solutions/141773/c-java-python-1-line-without-using-any-package-or/
        # Explanation: https://leetcode.com/problems/mirror-reflection/solutions/146336/java-solution-with-an-easy-to-understand-explanation/
        return ((p & -p) >= (q & -q)) + ((p & -p) > (q & -q))
