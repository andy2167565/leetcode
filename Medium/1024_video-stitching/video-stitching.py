class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # Reference: https://leetcode.com/problems/video-stitching/solutions/270036/java-c-python-greedy-solution-o-1-space/
        prev_end, end, ans = -1, 0, 0
        for i, j in sorted(clips):
            if end >= time or i > end:  # The clips have covered time or there is no consecutive clips available
                break
            elif prev_end < i <= end:  # Expand the coverage by the new consecutive clip
                ans, prev_end = ans + 1, end
            end = max(end, j)  # Update with the largest end
        return ans if end >= time else -1
