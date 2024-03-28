class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # Reference: https://leetcode.com/problems/longest-well-performing-interval/solutions/334565/java-c-python-o-n-solution-life-needs-996-and-669/
        ans = score = 0  # Find the longest interval that have strictly positive scores
        seen = {}  # seen[i]: The day that score i was seen for the first time
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                ans = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                ans = max(ans, i - seen[score - 1])
        return ans
