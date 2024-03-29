class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # Reference: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/solutions/720189/java-c-python-ants-keep-walking-o-n/
        return max(max(left, default=0), n - min(right, default=n))
