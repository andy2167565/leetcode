class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/solutions/944473/java-c-python-sort-and-some-story/
        tasks.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for a, m in tasks:
            ans = max(ans + a, m)
        return ans
