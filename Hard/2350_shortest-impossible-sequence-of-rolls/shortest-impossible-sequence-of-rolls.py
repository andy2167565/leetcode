class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/solutions/2322280/java-c-python-one-pass-o-k-space/
        ans, s = 1, set()
        for roll in rolls:
            s.add(roll)
            if len(s) == k:
                ans += 1
                s.clear()
        return ans
