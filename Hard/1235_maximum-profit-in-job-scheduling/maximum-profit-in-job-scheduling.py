class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
# Reference: https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/1430983/python-from-brute-force-to-dp-binary-search-clean-concise/
#======== <Solution 1> ========#
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))  # Sort by start time
        @cache
        def dp(i):  # Maximum profit of taking jobs in jobs[i, ..., n-1] such that there is no overlapping time range
            if i == n: return 0
            ans = dp(i + 1)  # Choice 1: Don't pick i-th job
            for j in range(i + 1, n + 1):
                if j == n or jobs[i][1] <= jobs[j][0]:  # First job in jobs[i + 1, ..., n] that does't overlap with i-th job
                    ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick i-th job
                    break
            return ans
        return dp(0)

#======== <Solution 2> ========#
        import bisect
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        startTime.sort()
        @cache
        def dp(i):
            if i == n: return 0
            ans = dp(i + 1)  # Choice 1: Don't pick i-th job
            j = bisect.bisect_left(startTime, jobs[i][1])
            ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick i-th job
            return ans
        return dp(0)
