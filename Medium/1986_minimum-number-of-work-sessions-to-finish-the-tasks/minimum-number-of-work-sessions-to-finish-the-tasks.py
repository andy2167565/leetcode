class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/solutions/1431829/python-dynamic-programming-on-subsets-explained/
        import functools
        n = len(tasks)

        @functools.cache
        def dp(mask):
            if not mask:
                return (1, 0)
            ans = (float('inf'), float('inf'))
            for j in range(n):
                if mask & (1 << j):
                    sessions, last = dp(mask - (1 << j))
                    full = (last + tasks[j] > sessionTime)
                    ans = min(ans, (sessions + full, tasks[j] + (1 - full) * last))
            return ans

        return dp((1 << n) - 1)[0]
