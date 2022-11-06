class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/minimum-total-distance-traveled/discuss/2783305/Python-DP-Solution
        robot.sort()
        factory.sort()
        @cache
        # i: Index of current robot
        # j: Index of current factory
        # k: Number of robots already fixed by current factory[j]
        def dp(i, j, k):
            if i == len(robot): return 0  # All robots are fixed
            if j == len(factory): return float('inf')  # No more available factory
            ans1 = dp(i, j + 1, 0)  # Skip current factory[j]
            ans2 = dp(i + 1, j, k + 1) + abs(robot[i] - factory[j][0]) if factory[j][1] > k else float('inf')  # Fix robot[i] in current factory[j] and then proceed to robot[i + 1]
            return min(ans1, ans2)
        return dp(0, 0, 0)

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/minimum-total-distance-traveled/discuss/2783245/Python3-O(MN)-DP
        import collections
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp[i][j]: Minimum moves to fix robot[i:] in factory[j:]
        for i in range(m):
            dp[i][-1] = float('inf')
        for j in range(n - 1, -1, -1):
            prefix = 0
            qq = collections.deque([(m, 0)])
            for i in range(m - 1, -1, -1):
                prefix += abs(robot[i] - factory[j][0])
                if qq[0][0] > i + factory[j][1]:
                    qq.popleft()
                while qq and qq[-1][1] >= dp[i][j + 1] - prefix:
                    qq.pop()
                qq.append((i, dp[i][j + 1] - prefix))
                dp[i][j] = qq[0][1] + prefix
        return dp[0][0]

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/minimum-total-distance-traveled/discuss/2783308/Python-assignment-problem-with-scipy
        from scipy import optimize
        import numpy
        costs = []
        for i, k in factory:
            c = [abs(j - i) for j in robot]
            for _ in range(k):
                costs.append(c)
        costs = numpy.array(costs)
        return costs[optimize.linear_sum_assignment(costs)].sum()
